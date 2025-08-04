#!/bin/bash
echo "🚀 Starting CADinfra FastAPI server..."
uvicorn server.main:app --host 0.0.0.0 --port 8000