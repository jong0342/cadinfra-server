#!/bin/bash
echo "🚀 Starting CADinfra FastAPI server..."

# 실행 (Render는 프로젝트 루트를 기준으로 실행되므로 server.main 형식 사용)
exec uvicorn server.main:app --host=0.0.0.0 --port=10000
