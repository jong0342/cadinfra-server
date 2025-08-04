# server/auth.py

from fastapi import APIRouter, Depends, HTTPException, status, Form
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from server import models, schemas
from server.database import get_db
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter(prefix="/auth", tags=["auth"])

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ✅ (1) 로그인 페이지 (GET)
@router.get("/login", response_class=HTMLResponse)
async def login_page():
    return """
    <html>
        <head><title>CADinfra 로그인</title></head>
        <body>
            <h2>✅ CADinfra FastAPI Login</h2>
            <form method="post" action="/auth/login">
                <label>아이디: <input type="text" name="username" /></label><br />
                <label>비밀번호: <input type="password" name="password" /></label><br />
                <button type="submit">로그인</button>
            </form>
        </body>
    </html>
    """


# ✅ (2) 로그인 처리 (POST)
@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


# ✅ (3) 회원가입 페이지 (GET)
@router.get("/register", response_class=HTMLResponse)
async def register_page():
    return """
    <html>
        <head><title>회원가입</title></head>
        <body>
            <h2>📝 CADinfra 회원가입</h2>
            <form method="post" action="/auth/register">
                <label>아이디: <input type="text" name="username" /></label><br />
                <label>비밀번호: <input type="password" name="password" /></label><br />
                <button type="submit">가입하기</button>
            </form>
        </body>
    </html>
    """


# ✅ (4) 회원가입 처리 (POST)
@router.post("/register")
def register(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user:
        raise HTTPException(status_code=400, detail="이미 존재하는 사용자입니다.")

    hashed_password = pwd_context.hash(password)
    new_user = models.User(username=username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "회원가입이 완료되었습니다."}


# ✅ (5) JWT 토큰 생성 함수
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
