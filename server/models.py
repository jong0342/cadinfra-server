# server/models.py

from sqlalchemy import Column, String
from server.database import Base

class User(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, index=True)
    hashed_password = Column(String, nullable=False)
