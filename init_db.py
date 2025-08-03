# init_db.py

from server.database import Base, engine
from server import models

def init():
    print("📦 데이터베이스 초기화 중...")
    Base.metadata.create_all(bind=engine)
    print("✅ 데이터베이스 초기화 완료 (cadinfra.db 생성됨)")

if __name__ == "__main__":
    init()
