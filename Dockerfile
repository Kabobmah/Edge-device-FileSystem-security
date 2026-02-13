FROM python:3.9-slim
WORKDIR /app
RUN python -m pip install requests flask
COPY . .
CMD ["python", "edge_device.py"]