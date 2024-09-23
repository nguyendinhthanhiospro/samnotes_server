from sqlalchemy import Boolean, Column, ForeignKey, Integer, Text

from source import db


class Colors(db.Model):
    __tablename__ = "color"
    idColor = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    r = Column(Integer)
    g = Column(Integer)
    b = Column(Integer)
