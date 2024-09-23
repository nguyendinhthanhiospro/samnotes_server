from source import db
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Boolean,
    DateTime,
    Float,
    Text,
)
from source.main.model.users import Users
from source.main.model.groups import Groups
from source.main.model.floders import Folder
from sqlalchemy.sql import func

from sqlalchemy.orm import relationship


class Notes(db.Model):
    __tablename__ = "notes"
    idNote = Column(Integer, primary_key=True, autoincrement=True)
    idFolder = Column(Integer, ForeignKey(Folder.id), nullable=False)
    idUser = Column(Integer, ForeignKey(Users.id), nullable=False)
    idGroup = Column(Integer, ForeignKey(Groups.idGroup), nullable=True)
    type = Column(String(20), nullable=False)
    title = Column(String(100), nullable=False)
    pinned = Column(Boolean, nullable=False, default=0)
    dueAt = Column(DateTime(timezone=True))
    r = Column(Integer, nullable=False)
    g = Column(Integer, nullable=False)
    b = Column(Integer, nullable=False)
    a = Column(Float, nullable=False, default=0)
    lock = Column(String(200))
    notePublic = Column(Integer, nullable=True)
    metaData = Column(Text, nullable=True)
    remindAt = Column(DateTime(timezone=True))
    doneNote = Column(Boolean, nullable=False, default=0)
    inArchived = Column(Boolean, nullable=False, default=1)
    createAt = Column(DateTime(timezone=True), default=func.now())
    updateAt = Column(DateTime(timezone=True), default=func.now())
    datas = relationship("Datas", backref="notes", lazy=True, cascade="all, delete")
    linkNoteShare = Column(Text, nullable=True)
    view = Column(Integer, nullable=False, default=0)
    # state=Column(Boolean, nullable=False, default=0)
    notes_comment = relationship("Comments", backref="notes")
    # images = relationship("Images", backref="notes", lazy=True, cascade="all, delete")
