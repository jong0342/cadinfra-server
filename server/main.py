from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.database import engine
from server import models
from server.auth import router as auth_router

app = FastAPI()

# DB 테이블 생성
models.Base.metadata.create_all(bind=engine)

# CORS 허용 설정
origins = [
    "http://localhost:3000",
    "https://cadinfra-client.onrender.com",
    "https://cadinfra.netlify.app",
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

@app.get("/")
def read_root():
    return {"message": "CADinfra backend is running"}
