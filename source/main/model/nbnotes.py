from source import db
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime,Float,Text
from source.main.model.users import Users

from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

class Nbnotes(db.Model):
    __tablename__ = 'nbnotes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idUser = Column(Integer, ForeignKey(Users.id), nullable=False)
    nbnotes=Column(Integer, nullable=True, default=0)
    user=relationship('Users',backref='nbnotes',lazy=True, cascade="all, delete")