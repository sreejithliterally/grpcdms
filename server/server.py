import grpc
from concurrent import futures
from sqlalchemy.orm import sessionmaker
import dms_pb2
import dms_pb2_grpc
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from contextlib import contextmanager
from passlib.hash import bcrypt
import jwt
from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError
from functools import wraps
from grpc import ServicerContext

from models import Base,User,File,Folder
from utils import verify




@contextmanager
def get_db():
    engine = create_engine("postgresql://postgres:something@localhost:5432/grpcdms")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
    finally:
        session.close()

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
TOKEN_EXPIRATION = timedelta(days=1)



class ErrorResponse:
    def __init__(self, success=False, message="Authentication failed"):
        self.success = success
        self.message = message

def authenticate_user(func):
    @wraps(func)
    def wrapper(self, request, context):
        try:
            # Debugging
            print("Received gRPC Request: ", context.invocation_metadata())

            # Extracting JWT token from the request metadata
            metadata = dict(context.invocation_metadata())
            jwt_token = metadata.get('authorization', '')

            # Debugging
            print(f"Received Token: {jwt_token}")

            # Verify and decode the JWT 
            decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM])

            # Debug
            print(f"Decoded Token: {decoded_token}")

          
            user_id = decoded_token.get('user_id')

      
            return func(self, request, context, user_id)
        except Exception as e:
            # Debug
            print(f"Authentication failed: {str(e)}")

        
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details(f"Authentication failed: {str(e)}")
            return ErrorResponse(success=False, message="Authentication failed")

    return wrapper





class DmsServiceServicer(dms_pb2_grpc.DmsServiceServicer):
    def __init__(self):
        self.Session = sessionmaker(autocommit=False, autoflush=False)

    def SayHello(self, request, context):
        test = dms_pb2.HelloResponse(message="Hello from the DMS server!")
        print(test)
        return test
    
    
    
      
    def Login(self, request, context):
        try:
            with get_db() as session:
               
                user = session.query(User).filter_by(username=request.username).first()

                
                if user and verify(request.password, user.password):
          
                    token = self.create_jwt_token(user.id)
                    return dms_pb2.LoginResponse(success=True, token=token, message="Authentication successful")
                else:
                    return dms_pb2.LoginResponse(success=False, message="Authentication failed")
        except SQLAlchemyError as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Database error: {str(e)}")
            return dms_pb2.AuthResponse(success=False, message="Internal server error")

    def create_jwt_token(self, user_id):
       
        payload = {
            "user_id": user_id,
            "exp": datetime.utcnow()+TOKEN_EXPIRATION
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return token


    
    
    def CreateUser(self, request, context): 
        with get_db() as session:
            
        
            existing_user = session.query(User).filter_by(username=request.username).first()
            if existing_user:
                context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                context.set_details("User with this username already exists")
                return dms_pb2.CreateUserResponse(message="Username already exists")

            hashed_password = bcrypt.hash(request.password)

           
            new_user = User(username=request.username, password=hashed_password)
            session.add(new_user)
            session.commit()
            return dms_pb2.CreateUserResponse(message="User created successfully")


    def GetUser(self, request, context):
        with get_db() as session:
           
            user = session.query(User).filter_by(id=user_id).first()
            if user:
                return dms_pb2.UserResponse(user_id=user.id, username=user.username)
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("User not found")
                return dms_pb2.UserResponse()
    
    @authenticate_user       
    def GetFolders(self, request, context,user_id):
        with get_db() as session:
          
            folders = session.query(Folder).filter_by(user_id=user_id).all()
            folder_protos = [dms_pb2.Folder(folder_id=folder.id, name=folder.name) for folder in folders]
            return dms_pb2.FolderResponse(folders=folder_protos)
    
    @authenticate_user
    def GetFiles(self, request, context, user_id):
        with get_db() as session:
            files = session.query(File).filter_by(folder_id=request.folder_id).all()

            # Debugging
            for file in files:
                print(f"File ID: {file.id}, Name: {file.name}")

            file_protos = [dms_pb2.File(file_id=file.id, name=file.name) for file in files]
            return dms_pb2.FileResponse(files=file_protos)

 
    def CreateFile(self, request, context):
        with get_db() as session:
            folder = session.query(Folder).filter_by(id=request.folder_id).first()
           
            if folder:
                new_file = File(name=request.filename, content=request.content, folder_id=request.folder_id)
                session.add(new_file)
                session.commit()
                return dms_pb2.CreateFileResponse(message="File created successfully",success=True)
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Folder not found")
                return dms_pb2.CreateFileResponse()

    def CreateFolder(self, request, context):
        with get_db() as session:
            
            new_folder = Folder(name=request.name, user_id=request.user_id)
            session.add(new_folder)
            session.commit()
            return dms_pb2.CreateFolderResponse(message="Folder created successfully", success=True)
        

    def MoveFile(self, request, context):
        with get_db() as session:
           
            file = session.query(File).filter_by(id=request.file_id).first()
            folder = session.query(Folder).filter_by(id=request.folder_id).first()
            if file and folder:
                file.folder_id = request.folder_id
                session.commit()
                return dms_pb2.MoveFileResponse(message="File moved successfully")
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("File or Folder not found")
                return dms_pb2.MoveFileResponse()


def serve():
    print("Starting gRPC server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dms_pb2_grpc.add_DmsServiceServicer_to_server(DmsServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Waiting for incoming requests...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()