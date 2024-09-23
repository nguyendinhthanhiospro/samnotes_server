from source import db
from sqlalchemy import Column, Integer, ForeignKey, Boolean,String,Text
from source.main.model.users import Users

from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

class Token_device(db.Model):
    __tablename__ = 'token_device'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idUser=Column(Integer, ForeignKey(Users.id),nullable=False)
    device=Column(String(50), nullable=False )
    tokenid=Column(Text, nullable=False )
    device_id = relationship("Users", backref="token_device")