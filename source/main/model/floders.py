from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from source import db
from sqlalchemy.orm import relationship
from source.main.model.users import Users


class Folder(db.Model):
    __tablename__ = 'folders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idUser = Column(Integer, ForeignKey(Users.id), nullable=False)
    nameFolder = Column(Text, nullable=True)
    createAt=Column(DateTime(timezone=True),default=func.now())
    folder_note=relationship('Notes',backref='folder',lazy=True)