# server/main.py

from fastapi import FastAPI
from .auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# CORS 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(auth_router)
