from app.db.database import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import false


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    is_admin = Column(Boolean, nullable=False, default=False)
    password = Column(String)

    builds = relationship("Build", cascade="all, delete-orphan", back_populates="user")
