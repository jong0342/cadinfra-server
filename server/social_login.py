# server/social_login.py
from fastapi import APIRouter, HTTPException
from server.utils import create_access_token

router = APIRouter()

@router.post("/social-login/{provider}")
def social_login(provider: str, token: str):
    # 여기선 예시용 로직만 포함됨 (진짜 인증은 OAuth 처리 필요)
    if provider not in ["google", "naver"]:
        raise HTTPException(status_code=400, detail="지원되지 않는 소셜 로그인 제공자입니다.")
    
    if token != "valid_social_token":
        raise HTTPException(status_code=401, detail="소셜 인증 실패")

    # 소셜 계정 이메일을 기반으로 토큰 생성 (예시)
    fake_email = f"{provider}_user@example.com"
    access_token = create_access_token(fake_email)
    return {"access_token": access_token}
