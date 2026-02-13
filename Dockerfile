FROM python:3.9-slim
WORKDIR /app
RUN pip install requests flask cryptography
COPY . .
CMD ["python", "edge_device.py"]