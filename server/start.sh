#!/bin/bash

# 실행 디렉토리로 이동 (이 스크립트가 있는 위치 기준)
cd "$(dirname "$0")"

# FastAPI 앱 실행 (포트 10000번, 외부 접속 허용)
uvicorn main:app --host 0.0.0.0 --port 10000
