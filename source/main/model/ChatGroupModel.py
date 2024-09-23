from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func

from source import db
from source.main.model.groups import Groups


class ChatGroupModel(db.Model):
    __tablename__ = "chats"
    idGroup = Column(Integer, ForeignKey(Groups.idGroup), nullable=False)
    idMes = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    text = Column(Text, nullable=True)
    image = Column(Text, nullable=True)
    gif = Column(Text, nullable=True)
    type = Column(Text, nullable=False, default="text")
    idSend = Column(Integer, nullable=False)
    listIdUserReaded = Column(Text, nullable=True)
    sendAt = Column(DateTime(timezone=True), default=func.now())
