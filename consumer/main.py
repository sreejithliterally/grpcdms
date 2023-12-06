
from fastapi import FastAPI, Depends, HTTPException,Form,Header
from fastapi.responses import JSONResponse
from grpc import insecure_channel
from dms_pb2 import UserRequest, FolderRequest, FileRequest, CreateFileRequest, CreateFolderRequest, MoveFileRequest, HelloRequest, CreateUserRequest,LoginRequest
from dms_pb2_grpc import DmsServiceStub



app = FastAPI()

def get_grpc_stub():
    channel = insecure_channel("localhost:50051")
    print(channel)
    return DmsServiceStub(channel)

@app.post("/login")
def authenticate_user(username: str = Form(...), password: str = Form(...), stub: DmsServiceStub = Depends(get_grpc_stub)):
    try:
        
        request = LoginRequest(username=username, password=password)

        response = stub.Login(request)

   
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




@app.post("/create_user")
def create_user(username: str, password: str, stub: DmsServiceStub = Depends(get_grpc_stub)):
    try:
        request = CreateUserRequest(username=username, password=password)
        response = stub.CreateUser(request)
        return JSONResponse(content={"message": response.message})
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

@app.get("/get_folders/{user_id}")
async def get_folders(user_id: int,stub: DmsServiceStub = Depends(get_grpc_stub)):
    try:
        
        request = FolderRequest(user_id=user_id)
        response = stub.GetFolders(request)
        folders = [{"folder_id": folder.folder_id, "name": folder.name} for folder in response.folders]
        return JSONResponse(content={"folders": folders})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/get_files/{folder_id}")
async def get_files(folder_id: int, stub: DmsServiceStub = Depends(get_grpc_stub)):
    try:
        request = FileRequest(folder_id=folder_id)
        response = stub.GetFiles(request)
        files = [{"file_id": file.file_id, "name": file.name} for file in response.files]
        return JSONResponse(content={"files": files})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

