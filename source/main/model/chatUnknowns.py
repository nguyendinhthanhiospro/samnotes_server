from sqlalchemy import Column, DateTime, ForeignKey, Integer, LargeBinary, String, Text
from sqlalchemy.sql import func
from source.main.model.users import Users
from source import db
import random
import string
from sqlalchemy.orm import relationship


def generate_random_id(length):
    characters = string.ascii_letters + string.digits  # Bao gồm chữ cái và chữ số
    random_id = "".join(random.choice(characters) for _ in range(length))
    return random_id


class ChatUnknowns(db.Model):
    __tablename__ = "chatunknowns"
    idReceive = Column(Integer, ForeignKey(Users.id), nullable=False)
    idMes = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    idSend = Column(Text, nullable=False, default=generate_random_id(10))
    idRoom = Column(Text, nullable=True)
    text = Column(Text, nullable=True)
    img = Column(Text, nullable=True)
    gif = Column(Text, nullable=True)
    type = Column(Text, nullable=True)
    status = Column(Text, nullable=True, default="seen")
    sendAt = Column(DateTime(timezone=True), default=func.now())
    user = relationship("Users", backref="chatunknowns")
