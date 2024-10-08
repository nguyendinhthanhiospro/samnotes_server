from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func

from source import db
from source.main.model.users import Users
from source.main.model.groups import Groups
from sqlalchemy.orm import relationship


class Members(db.Model):
    __tablename__ = "members"
    idMember = Column(Integer, primary_key=True, autoincrement=True)
    idGroup = Column(
        Integer,
        ForeignKey(Groups.idGroup),
        nullable=False,
    )
    idUser = Column(Integer, ForeignKey(Users.id), nullable=False)
    role = Column(String(50), nullable=False, default="Member")
    createAt = Column(DateTime(timezone=True), default=func.now())
    gmail = Column(String(255), nullable=True)
    groups = relationship("Groups", backref="groups", lazy=True, cascade="all, delete")
    idUserAddMe = Column(Integer, ForeignKey(Users.id), nullable=False)
