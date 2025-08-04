from pydantic import BaseModel, EmailStr


# ▶ 회원가입 요청
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# ▶ 로그인 요청
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ▶ 로그인 성공 시 반환
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ▶ 사용자 응답 스키마
class User(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True
