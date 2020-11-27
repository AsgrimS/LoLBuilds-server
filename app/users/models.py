from enum import unique

from app.db.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref, relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    password = Column(String)

    builds = relationship("Build", cascade="all, delete-orphan")
