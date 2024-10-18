from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func

from source import db
from source.main.model.users import Users


class Favorites_Note(db.Model):
    __tablename__ = "favorite_note"
    id = Column(Integer, primary_key=True, autoincrement=True)
    idNote = Column(Integer, nullable=False)
    idUser = Column(Integer, ForeignKey(Users.id), nullable=False)
    type = Column(Enum("like", "dislike"), nullable=True)
