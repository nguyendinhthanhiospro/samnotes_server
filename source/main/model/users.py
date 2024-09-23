import datetime

import jwt
from sqlalchemy import Column, DateTime, Float, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from source import app, db


class Users(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    gmail = Column(String(70))
    user_name = Column(String(50))
    password_hash = Column(String(200), nullable=False)
    password_hash_2 = Column(String(200), nullable=True)
    notes = relationship("Notes", backref="users", lazy=True, cascade="all, delete")
    r = Column(Integer, nullable=False, default=255)
    g = Column(Integer, nullable=False, default=125)
    b = Column(Integer, nullable=False, default=125)
    a = Column(Float, nullable=False, default=0.87)
    df_screen = Column(String(20), default="Archived")
    df_fontsize = Column(String(20), default="Default")
    createAt = Column(DateTime(timezone=True), default=func.now())
    linkAvatar = Column(
        Text,
        nullable=False,
        default=f"https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png",
    )
    linkAvtprofile = Column(
        Text,
        nullable=False,
        default=f"https://luanvanviet.com/wp-content/uploads/2020/11/hinh-anh-cac-loai-hinh-du-lich-3.jpg",
    )
    statesLogin = Column(Boolean, nullable=False)
    last_activity_time = Column(DateTime, default=func.now())
    user_comment = relationship("Comments", backref="users")
    folder = relationship("Folder", backref="users", lazy=True, cascade="all, delete")
    isBlockAllUnknow = Column(Integer, nullable=False)
