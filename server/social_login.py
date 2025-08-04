# server/social_login.py
"""Social login route and utilities.

This module provides a very small mock of a social login endpoint. During a
recent refactor the function responsible for issuing JWT tokens was renamed to
``create_token`` in :mod:`server.utils`. However this module still attempted to
import the old name ``create_access_token`` which no longer exists, causing an
``ImportError`` at runtime.

To fix the bug we now import ``create_token`` and use it when generating the
fake access token. This keeps the example endpoint working and reflects the
current naming in ``server.utils``.
"""

from fastapi import APIRouter, HTTPException
from server.utils import create_token

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
    access_token = create_token(fake_email)
    return {"access_token": access_token}
