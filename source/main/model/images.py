from sqlalchemy import Boolean, Column, ForeignKey, Integer, Text

from source import db
from source.main.model.notes import Notes
from source.main.model.users import Users


class Images(db.Model):
    __tablename__ = "images"
    idImage = Column(Integer, primary_key=True, autoincrement=True)
    idNote = Column(Integer, ForeignKey(Notes.idNote), nullable=False)
    link = Column(Text)
    idUserUpload = Column(Integer, ForeignKey(Users.id), nullable=False)
