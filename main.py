# main.py - CADinfra 프로그램 실행 진입점
import os
import json
from gui.login import show_login_window

# 사용자 설정 파일 경로
TOKEN_FILE = "token.json"
CONFIG_FILE = "user_config.json"

# 프로그램 시작 시 토큰 파일 초기화
def clear_token_if_needed():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            try:
                data = json.load(f)
                if not data.get("token"):
                    os.remove(TOKEN_FILE)
            except json.JSONDecodeError:
                os.remove(TOKEN_FILE)

if __name__ == "__main__":
    clear_token_if_needed()
    show_login_window()
