#!/bin/bash
set -e
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
DOCKER_IMAGE="order-validation-fastapi:latest"
docker build -t $DOCKER_IMAGE .
docker rm -f order-validation-app 2>/dev/null || true
docker run -d --name order-validation-app -p 8000:8000 $DOCKER_IMAGE
