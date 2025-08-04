from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    model_config = ConfigDict(from_attributes=True)  # ✅ Pydantic v2 대응

class Token(BaseModel):
    access_token: str
    token_type: str
