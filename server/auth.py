# server/auth.py

from fastapi import APIRouter, Depends, HTTPException, Header, status
from sqlalchemy.orm import Session
from server import models, schemas
from server.database import get_db
from server.utils import hash_password, verify_password, create_token, decode_token

router = APIRouter()

# ✅ 회원가입
@router.post("/register")
def register_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    email = request.email.lower()
    user = db.query(models.User).filter(models.User.email == email).first()
    if user:
        raise HTTPException(status_code=400, detail="이미 가입된 이메일입니다.")
    
    new_user = models.User(
        email=email,
        hashed_password=hash_password(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "회원가입 완료"}

# ✅ 로그인
@router.post("/login")
def login_user(request: schemas.UserLogin, db: Session = Depends(get_db)):
    email = request.email.lower()
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="이메일 또는 비밀번호가 잘못되었습니다.")
    
    token = create_token(user.email)
    return {"access_token": token}

# ✅ 유저 정보 조회 (토큰 기반)
@router.get("/me")
def get_my_info(authorization: str = Header(...), db: Session = Depends(get_db)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="유효하지 않은 인증 헤더입니다.")

    token = authorization.split(" ")[1]
    try:
        payload = decode_token(token)
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=400, detail="토큰에 이메일 정보가 없습니다.")
        
        user = db.query(models.User).filter(models.User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")
        
        return {"email": user.email}
    
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"인증 실패: {str(e)}")
