from app.db.database import Base
from sqlalchemy import Column, Integer, String


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    plaintext = Column(String)
    image = Column(String)
