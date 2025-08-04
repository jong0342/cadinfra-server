from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ SQLite 사용 예시 (기본 local 파일)
SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"

# 만약 PostgreSQL 사용 시 아래와 같이 구성
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@host:port/dbname"

# connect_args는 SQLite에만 필요 (다른 DB는 제거)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
