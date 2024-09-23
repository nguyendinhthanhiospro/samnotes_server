from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func

from source import db
from source.main.model.groups import Groups


class block_unknow(db.Model):
    __tablename__ = "block_unknow"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    idUserOwner = Column(Integer, nullable=False)
    idUserBlock = Column(Integer, nullable=True)
    Reason = Column(Text, nullable=True)
    createdAt = Column(DateTime(timezone=True), default=func.now())
