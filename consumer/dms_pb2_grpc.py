# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dms_pb2 as dms__pb2


class DmsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUser = channel.unary_unary(
                '/dms.DmsService/GetUser',
                request_serializer=dms__pb2.UserRequest.SerializeToString,
                response_deserializer=dms__pb2.UserResponse.FromString,
                )
        self.GetFolders = channel.unary_unary(
                '/dms.DmsService/GetFolders',
                request_serializer=dms__pb2.FolderRequest.SerializeToString,
                response_deserializer=dms__pb2.FolderResponse.FromString,
                )
        self.GetFiles = channel.unary_unary(
                '/dms.DmsService/GetFiles',
                request_serializer=dms__pb2.FileRequest.SerializeToString,
                response_deserializer=dms__pb2.FileResponse.FromString,
                )
        self.CreateFile = channel.unary_unary(
                '/dms.DmsService/CreateFile',
                request_serializer=dms__pb2.CreateFileRequest.SerializeToString,
                response_deserializer=dms__pb2.CreateFileResponse.FromString,
                )
        self.CreateFolder = channel.unary_unary(
                '/dms.DmsService/CreateFolder',
                request_serializer=dms__pb2.CreateFolderRequest.SerializeToString,
                response_deserializer=dms__pb2.CreateFolderResponse.FromString,
                )
        self.MoveFile = channel.unary_unary(
                '/dms.DmsService/MoveFile',
                request_serializer=dms__pb2.MoveFileRequest.SerializeToString,
                response_deserializer=dms__pb2.MoveFileResponse.FromString,
                )
        self.SayHello = channel.unary_unary(
                '/dms.DmsService/SayHello',
                request_serializer=dms__pb2.HelloRequest.SerializeToString,
                response_deserializer=dms__pb2.HelloResponse.FromString,
                )
        self.CreateUser = channel.unary_unary(
                '/dms.DmsService/CreateUser',
                request_serializer=dms__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=dms__pb2.CreateUserResponse.FromString,
                )
        self.Login = channel.unary_unary(
                '/dms.DmsService/Login',
                request_serializer=dms__pb2.LoginRequest.SerializeToString,
                response_deserializer=dms__pb2.LoginResponse.FromString,
                )


class DmsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFolders(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFolder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MoveFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DmsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=dms__pb2.UserRequest.FromString,
                    response_serializer=dms__pb2.UserResponse.SerializeToString,
            ),
            'GetFolders': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFolders,
                    request_deserializer=dms__pb2.FolderRequest.FromString,
                    response_serializer=dms__pb2.FolderResponse.SerializeToString,
            ),
            'GetFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFiles,
                    request_deserializer=dms__pb2.FileRequest.FromString,
                    response_serializer=dms__pb2.FileResponse.SerializeToString,
            ),
            'CreateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFile,
                    request_deserializer=dms__pb2.CreateFileRequest.FromString,
                    response_serializer=dms__pb2.CreateFileResponse.SerializeToString,
            ),
            'CreateFolder': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFolder,
                    request_deserializer=dms__pb2.CreateFolderRequest.FromString,
                    response_serializer=dms__pb2.CreateFolderResponse.SerializeToString,
            ),
            'MoveFile': grpc.unary_unary_rpc_method_handler(
                    servicer.MoveFile,
                    request_deserializer=dms__pb2.MoveFileRequest.FromString,
                    response_serializer=dms__pb2.MoveFileResponse.SerializeToString,
            ),
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=dms__pb2.HelloRequest.FromString,
                    response_serializer=dms__pb2.HelloResponse.SerializeToString,
            ),
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=dms__pb2.CreateUserRequest.FromString,
                    response_serializer=dms__pb2.CreateUserResponse.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=dms__pb2.LoginRequest.FromString,
                    response_serializer=dms__pb2.LoginResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dms.DmsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DmsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dms.DmsService/GetUser',
            dms__pb2.UserRequest.SerializeToString,
            dms__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFolders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dms.DmsService/GetFolders',
            dms__pb2.FolderRequest.SerializeToString,
            dms__pb2.FolderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dms.DmsService/GetFiles',
            dms__pb2.FileRequest.SerializeToString,
            dms__pb2.FileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dms.DmsService/CreateFile',
            dms__pb2.CreateFileRequest.SerializeToString,
            dms__pb2.CreateFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateFolder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dms.DmsService/CreateFolder',
            dms__pb2.CreateFolderRequest.SerializeToString,
            dms__pb2.CreateFolderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MoveFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dms.DmsService/MoveFile',
            dms__pb2.MoveFileRequest.SerializeToString,
            dms__pb2.MoveFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dms.DmsService/SayHello',
            dms__pb2.HelloRequest.SerializeToString,
            dms__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dms.DmsService/CreateUser',
            dms__pb2.CreateUserRequest.SerializeToString,
            dms__pb2.CreateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dms.DmsService/Login',
            dms__pb2.LoginRequest.SerializeToString,
            dms__pb2.LoginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
