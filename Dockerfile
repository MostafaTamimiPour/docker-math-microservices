# Dockerfile for controller
FROM python:3.9-slim
WORKDIR /app
COPY controller.py /app
RUN pip install --no-cache-dir requests
CMD ["python", "controller.py"]
