FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*