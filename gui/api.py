# gui/api.py

import os
import requests

# 환경 변수로 주소 전환 가능
BASE_URL = "https://cadinfra-server.onrender.com"
if os.getenv("USE_LOCALHOST") == "1":
    BASE_URL = "http://127.0.0.1:8000"

def login(username: str, password: str):
    try:
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={"username": username, "password": password},
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise ConnectionError(f"서버에 연결할 수 없습니다:\n{e}")
