#!/bin/bash
set -e
./install.sh
if docker ps | grep order-validation-app >/dev/null 2>&1; then
  echo "Order Validation FastAPI app is running at http://localhost:8000 ."
else
  echo "Failed to start the Order Validation FastAPI app." >&2
  exit 1
fi
