# server/main.py - Render 배포용 FastAPI 서버 진입점

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth import router as auth_router
from server.social_login import router as social_router

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발 중에는 * 허용, 운영에서는 도메인 지정
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(auth_router)
app.include_router(social_router, prefix="/social")

# 기본 루트 테스트용
@app.get("/")
def read_root():
    return {"message": "CADinfra FastAPI server is running"}
