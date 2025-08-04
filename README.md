# CADinfra 서버 및 GUI

CAD 기반 파이프 설계 및 자동화를 위한 통합 솔루션입니다.  
ZWCAD + Python + FastAPI + SQLite 기반으로 구성되어 있으며, GUI 및 백엔드를 분리하여 유지 보수가 용이합니다.

## 기능

- ✅ 서버 기반 로그인 및 회원가입 (JWT 인증)
- ✅ 로그인 토큰 자동 저장 및 재사용
- ✅ GUI에서 CAD 블럭 삽입 및 시트 기반 작업
- ✅ 전개도 자동 처리 예정

## 설치 및 실행 방법

### 1. 가상환경 생성 및 패키지 설치

```bash
python -m venv venv
venv\Scripts\activate
pip install -r server/requirements.txt
