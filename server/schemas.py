from pydantic import BaseModel

# 🔐 회원가입 시 요청 구조
class UserCreate(BaseModel):
    username: str
    password: str

# 🙍 회원 응답 구조
class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

# 🔑 로그인 후 반환할 토큰 구조
class Token(BaseModel):
    access_token: str
    token_type: str
