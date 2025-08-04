# server/main.py - FastAPI 서버 진입점

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .auth import router as auth_router
from .social_login import router as social_router
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CADinfra API Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, tags=["인증"])
app.include_router(social_router, tags=["소셜"])
