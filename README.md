# 🚀 CADinfra - ZWCAD 기반 파이프 설계 도구

**CADinfra**는 Python 기반으로 개발된 파이프 및 구조물 설계 자동화 도구입니다.  
ZWCAD와 연동되는 블록 삽입, 엑셀 기반 전개도 처리, 로그인 인증 서버까지 포함합니다.

---

## 📦 주요 기능

- ✅ Excel 전개도 시트 불러오기 및 TreeView 미리보기
- ✅ CAD 명령어 전개 (ZWCAD 연동 가능)
- ✅ FastAPI 서버 기반 로그인 / 회원가입
- ✅ 자동 로그인, 아이디 저장 기능
- ✅ JWT 기반 유저 인증
- ✅ SQLite DB 연동
- ✅ Render 무료 서버 배포 연동

---

## 🧑‍💻 기술 스택

| 구성 요소 | 기술 |
|-----------|------|
| GUI       | `Tkinter`, `Pandas`, `ttk`  
| 백엔드    | `FastAPI`, `SQLite`, `SQLAlchemy`, `JWT`, `bcrypt`  
| 배포      | `Render`, `GitHub`, `.env` 환경 변수  

---

## 🛠️ 설치 방법 (개발환경)

```bash
git clone https://github.com/jong0342/cadinfra-server.git
cd cadinfra-server
pip install -r server/requirements.txt
