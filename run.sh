#!/bin/bash

# 1. Wait for DB to be ready (simple sleep for safety)
echo "Waiting for database..."
sleep 5

# 2. Run ETL Pipeline (Fetch Data)
echo "Running ETL Pipeline..."
python -m app.etl.pipeline

# 3. Start the API Server
echo "Starting Web Server..."
uvicorn app.main:app --host 0.0.0.0 --port 8000