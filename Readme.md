# gRPC Document Management System (gRPCDMS)

Welcome to the gRPC Document Management System! This project provides a simple document management system using gRPC.

This project consists of two main components:

- **gRPC Server (server/):**
  - Handles document management functionalities using gRPC.
  - Uses PostgreSQL as the database backend.
  - Implemented in Python with FastAPI.

- **FastAPI Client (consumer/):**
  - Provides a web API for interacting with the gRPC server.
  - Communicates with the gRPC server using generated gRPC client stubs.
  - Implemented in Python with FastAPI.


  Getting Started

    Clone the repository:

    bash

git clone https://github.com/sreejithliterally/grpcdms.git
cd grpcdms

Build Docker images:

bash

docker-compose build

Run Docker containers:

bash

docker-compose up

Access FastAPI client at http://localhost:8000 and gRPC server at http://localhost:50051.