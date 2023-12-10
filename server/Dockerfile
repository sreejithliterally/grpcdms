FROM python:3.11.2

WORKDIR /usr/src/app


COPY . /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for gRPC
EXPOSE 50051

# Run the gRPC server when the container launches
CMD ["python3", "./server.py"]
