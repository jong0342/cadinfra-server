from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server import models
from server.database import engine
from server.auth import router as auth_router

# 데이터베이스 모델 생성
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS 설정 (프론트엔드와 연동 시 필요)
origins = [
    "http://localhost:3000",  # 로컬 프론트엔드
    "https://cadinfra.netlify.app",  # 실제 서비스 도메인 있다면 추가
    "https://cadinfra-client.onrender.com",
    # 추가 origin...
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(auth_router)

# 기본 루트
@app.get("/")
def read_root():
    return {"message": "CADinfra backend is running"}

