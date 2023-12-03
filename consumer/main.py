
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from grpc import insecure_channel
from dms_pb2 import UserRequest, FolderRequest, FileRequest, CreateFileRequest, CreateFolderRequest, MoveFileRequest, HelloRequest
from dms_pb2_grpc import DmsServiceStub



app = FastAPI()

def get_grpc_stub():
    channel = insecure_channel("localhost:50051")
    print(channel)
    return DmsServiceStub(channel)
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
async def get_folders(user_id: int, stub: DmsServiceStub = Depends(get_grpc_stub)):
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
