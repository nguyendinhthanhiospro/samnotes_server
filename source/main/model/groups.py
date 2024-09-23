from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from source import db


class Groups(db.Model):
    __tablename__ = "groups"
    idGroup = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    describe = Column(Text, nullable=True)
    linkAvatar = Column(Text, nullable=True)
    idOwner = Column(Integer, nullable=False)
    createAt = Column(DateTime(timezone=True), default=func.now())
    notes = relationship("Notes", backref="groups", lazy=True, cascade="all, delete")
    r = Column(Integer, default=255)
    g = Column(Integer, default=255)
    b = Column(Integer, default=255)
    a = Column(Float, default=0.99)
    idMemberOf_Owner = Column(Integer, nullable=False)
    last_time_chat = Column(DateTime(timezone=True), default=func.now())
