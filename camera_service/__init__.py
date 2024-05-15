from concurrent import futures
import logging
import toml

import grpc
from proto_services.camera_service_pb2 import IsCameraAliveResponse
from proto_services.camera_service_pb2_grpc import add_CameraServiceServicer_to_server, CameraServiceServicer
from camera_service.helpers.poetry_install import poetry_install
from camera_service.generate_code import generate_code
from google.protobuf import empty_pb2


class CameraService(CameraServiceServicer):
    def IsCameraAlive(self, request, context):
        return IsCameraAliveResponse(isAlive=True)
    def InstallModules(self, request, context):
        # Add packages from array to the project.
        
        with open('pyproject.toml', 'r') as file:
            pyproject_data = toml.load(file)
        for package in request.modules:
            pyproject_data['tool']['poetry']['dependencies'][package.name] = package.version

        with open('pyproject.toml', 'w') as file:
            toml.dump(pyproject_data, file)


        generate_code()


        
        return empty_pb2()


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_CameraServiceServicer_to_server(CameraService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


def start():
    logging.basicConfig()
    
    # Install packages.
    poetry_install()
    serve()