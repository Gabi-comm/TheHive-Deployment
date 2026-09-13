FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        docker.io \
        docker-compose-v2 && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir requests

WORKDIR /app
COPY src/deploy.py .

CMD ["python", "deploy.py"]
