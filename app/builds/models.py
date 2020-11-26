from app.db.database import Base
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

builditems_table = Table(
    "builditems",
    Base.metadata,
    Column("build_id", Integer, ForeignKey("builds.id")),
    Column("item_id", Integer, ForeignKey("items.id")),
)


class Build(Base):
    __tablename__ = "builds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))
    items = relationship("Item", secondary=builditems_table)
