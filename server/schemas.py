# server/schemas.py - Pydantic 스키마 정의

from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    email: EmailStr

    class Config:
        from_attributes = True  # orm_mode → from_attributes (Pydantic v2)
