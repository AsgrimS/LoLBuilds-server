from ast import Str

from app.db.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class Build(Base):
    __tablename__ = "builds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    items = relationship("BuildItem", cascade="all, delete")


class BuildItem(Base):
    __tablename__ = "builditems"
    id = Column(Integer, primary_key=True)
    comment = Column(String, nullable=True)
    build_id = Column(Integer, ForeignKey("builds.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    build = relationship("Build", back_populates="items")
    item = relationship("Item", lazy="subquery")
