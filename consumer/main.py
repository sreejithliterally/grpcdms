
from fastapi import FastAPI, Depends, HTTPException,Form,Header,Body
from fastapi.responses import JSONResponse
from grpc import insecure_channel
from dms_pb2 import UserRequest, FolderRequest, FileRequest, CreateFileRequest, CreateFolderRequest, MoveFileRequest, HelloRequest, CreateUserRequest,LoginRequest
from dms_pb2_grpc import DmsServiceStub
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

class CreateUserRequestModel(BaseModel):
    username: str
    password: str

class CreateUserResponseModel(BaseModel):
    message: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You might want to restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_jwt_token(x_token: str = Header(..., description="JWT token")):
    print(x_token)
    return x_token

def get_grpc_stub():
    channel = insecure_channel("localhost:50051")
    print(channel)
    return DmsServiceStub(channel)

@app.post("/login")
def authenticate_user(username: str = Form(...), password: str = Form(...), stub: DmsServiceStub = Depends(get_grpc_stub)):
    try:
        
        request = LoginRequest(username=username, password=password)
        print(request)
        response = stub.Login(request)
        print(response)
   
        if response.success:
            return {"message": "Authentication successful", "token": response.token}
        else:
            raise HTTPException(status_code=401, detail="Authentication failed")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.post("/create_folder")
async def create_folder(
    user_id: int = Form(...),
    folder_name: str = Form(...),
    # authorization: str = Header(...),
    stub: DmsServiceStub = Depends(get_grpc_stub),
):
    try:
       
        request = CreateFolderRequest(name=folder_name, user_id=user_id)

       
        response = stub.CreateFolder(request)
        print(response)
      
        if response.success:
            return {"message": response.message}
        else:
            raise HTTPException(status_code=500, detail=f"Error: {response.message}")

    except Exception as e:
        print(f"Exception details: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")




@app.post("/create_user", response_model=CreateUserResponseModel)
def create_user(user_info: CreateUserRequestModel, stub: DmsServiceStub = Depends(get_grpc_stub)):
    try:
        request = CreateUserRequest(username=user_info.username, password=user_info.password)
        response = stub.CreateUser(request)
        return CreateUserResponseModel(message=response.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.post("/create_file")
async def create_file(
    folder_id: int = Form(...),
    filename: str = Form(...),
    content: str = Form(...),
    stub: DmsServiceStub = Depends(get_grpc_stub),
):
    try:
      
        request = CreateFileRequest(
            folder_id=folder_id,filename=filename, content=content)
    

        
        response = stub.CreateFile(request)

       
        if response.success:
            return {"message": response.message}
        else:
            raise HTTPException(status_code=500, detail=f"Error: {response.message}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/say_hello")
async def say_hello(stub: DmsServiceStub = Depends(get_grpc_stub)):
    try:
        
        request = HelloRequest()
        response = stub.SayHello(request)
        return JSONResponse(content={"message": response.message})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@app.get("/get_user/{user_id}")
async def get_user(user_id: int, stub: DmsServiceStub = Depends(get_grpc_stub)):
    try:
        request = UserRequest(user_id=user_id)
        response = stub.GetUser(request)
        print(response)
        return JSONResponse(content={"user_id": response.user_id, "username": response.username})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/get_folders")
async def get_folders(token: str = Depends(get_jwt_token), stub: DmsServiceStub = Depends(get_grpc_stub)):
    try:
        # Debugging: Print the token before making the gRPC request
        print("Token before gRPC request: ", token)

        # Pass the token in the headers to gRPC
        metadata = [('authorization', token)]

        # Debugging: Print the headers before making the gRPC request
        print("Headers before gRPC request: ", metadata)

        # Make the gRPC request
        response = stub.GetFolders(FolderRequest(), metadata=metadata)
        folders = [{"folder_id": folder.folder_id, "name": folder.name} for folder in response.folders]
        return JSONResponse(content={"folders": folders})
    except Exception as e:
        print(metadata)
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@app.get("/get_files/{folder_id}")
async def get_files(folder_id: int,token: str = Depends(get_jwt_token), stub: DmsServiceStub = Depends(get_grpc_stub)):
    try:
        metadata = [('authorization', token)]
        request = FileRequest(folder_id=folder_id)
        response = stub.GetFiles(request,metadata=metadata)
        files = [{"file_id": file.file_id, "name": file.name} for file in response.files]
        return JSONResponse(content={"files": files})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

