FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    bash coreutils findutils python3 python3-pip \ && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY solution.sh /app/solution.sh
RUN chmod +x /app/solution.sh
