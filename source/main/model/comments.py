from sqlalchemy import Column, DateTime, ForeignKey, Integer, String,Text
from sqlalchemy.sql import func

from source import db
from source.main.model.users import Users
from source.main.model.notes import Notes
from sqlalchemy.orm import relationship

class Comments(db.Model):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idUser = Column(Integer, ForeignKey(Users.id), nullable=False)
    idNote = Column(Integer, ForeignKey(Notes.idNote), nullable=False)
    text=Column(Text,nullable=True)
    sendAt=Column(DateTime(timezone=True),default=func.now())
    parent_id = Column(Integer, nullable=True)