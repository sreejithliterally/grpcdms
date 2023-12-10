FROM python:3.11.2

WORKDIR /app

COPY main.py requirements.txt /app/
COPY dms_pb2.py dms_pb2_grpc.py /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Command to run the FastAPI client
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
