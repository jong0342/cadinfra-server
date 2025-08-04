# server/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.auth import router as auth_router
from server.social_login import router as social_router

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 운영시 허용 도메인으로 제한 가능
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(auth_router, prefix="/auth")
app.include_router(social_router, prefix="/social")

# 헬스체크 라우트
@app.get("/")
def read_root():
    return {"message": "✅ CADinfra FastAPI server is running"}
