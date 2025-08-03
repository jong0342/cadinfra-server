# server/utils.py

import bcrypt
from jose import jwt, JWTError
from fastapi import HTTPException

# JWT 설정
SECRET_KEY = "your_secret_key"  # 배포 시에는 반드시 .env에서 불러와야 함
ALGORITHM = "HS256"


# ✅ 비밀번호 해싱
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


# ✅ 비밀번호 검증
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


# ✅ 토큰 생성
def create_token(email: str) -> str:
    to_encode = {"sub": email}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# ✅ 토큰 디코딩
def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="토큰 디코딩 실패")
