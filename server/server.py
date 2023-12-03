import grpc
from concurrent import futures
from sqlalchemy.orm import sessionmaker
import dms_pb2
import dms_pb2_grpc
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from contextlib import contextmanager




Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    folders = relationship('Folder', back_populates='user')

class Folder(Base):
    __tablename__ = 'folders'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    user = relationship('User', back_populates='folders')
    files = relationship('File', back_populates='folder')

class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    content = Column(String, nullable=True)  # You might want to adjust the data type
    folder_id = Column(Integer, ForeignKey('folders.id'), nullable=False)

    folder = relationship('Folder', back_populates='files')


@contextmanager
def get_db():
    # Replace this with your actual database configuration
    engine = create_engine("postgresql://postgres:something@localhost:5432/grpcdms")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
    finally:
        session.close()




class DmsServiceServicer(dms_pb2_grpc.DmsServiceServicer):
    def __init__(self):
        self.Session = sessionmaker(autocommit=False, autoflush=False)

    def SayHello(self, request, context):
        return dms_pb2.HelloResponse(message="Hello from the DMS server!")
    
    def CreateUser(self, request, context):
        with get_db() as session:
            # Check if the username already exists
            existing_user = session.query(User).filter_by(username=request.username).first()
            if existing_user:
                context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                context.set_details("User with this username already exists")
                return dms_pb2.CreateUserResponse(message="Username already exists")

            # Create a new user
            new_user = User(username=request.username)
            session.add(new_user)
            session.commit()
            return dms_pb2.CreateUserResponse(message="User created successfully")


    def GetUser(self, request, context):
        with get_db() as session:
            user = session.query(User).filter_by(id=request.user_id).first()
            if user:
                return dms_pb2.UserResponse(user_id=user.id, username=user.username)
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("User not found")
                return dms_pb2.UserResponse()

    def GetFolders(self, request, context):
        with get_db() as session:
            folders = session.query(Folder).filter_by(user_id=request.user_id).all()
            folder_protos = [dms_pb2.Folder(folder_id=folder.id, name=folder.name) for folder in folders]
            return dms_pb2.FolderResponse(folders=folder_protos)

    def GetFiles(self, request, context):
        with get_db() as session:
            files = session.query(File).filter_by(folder_id=request.folder_id).all()
            file_protos = [dms_pb2.File(file_id=file.id, name=file.name) for file in files]
            return dms_pb2.FileResponse(files=file_protos)

    def CreateFile(self, request, context):
        with get_db() as session:
            folder = session.query(Folder).filter_by(id=request.folder_id).first()
            if folder:
                new_file = File(name=request.file.name, content=request.file.content, folder_id=request.folder_id)
                session.add(new_file)
                session.commit()
                return dms_pb2.CreateFileResponse(message="File created successfully")
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Folder not found")
                return dms_pb2.CreateFileResponse()

    def CreateFolder(self, request, context):
        with get_db() as session:
            new_folder = Folder(name=request.folder.name, user_id=request.user_id)
            session.add(new_folder)
            session.commit()
            return dms_pb2.CreateFolderResponse(message="Folder created successfully")

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

# Create a gRPC server and add the servicer
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