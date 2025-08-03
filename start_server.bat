@echo off
cd /d %~dp0
echo 🔄 FastAPI 서버 실행 중...
uvicorn server.main:app --reload
pause