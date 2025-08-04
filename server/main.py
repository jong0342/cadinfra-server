# server/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth import router as auth_router  # 상대경로 주의 (server/ 내부에 위치)

app = FastAPI(
    title="CADinfra API",
    description="CADinfra 로그인 및 인증 기능 제공",
    version="1.0.0"
)

# CORS 설정 (필요 시 수정 가능)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 배포 시 도메인 제한 가능
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 등록
app.include_router(auth_router, prefix="/auth")

# 기본 엔드포인트
@app.get("/")
def read_root():
    return {"message": "✅ CADinfra FastAPI 서버 정상 작동 중!"}
