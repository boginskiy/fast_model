from datetime import datetime

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Table
# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,
from sqlalchemy.orm import relationship
from user.models import users
from sqlalchemy.sql import func
from core.db import metadata

parsers = Table(
    "parsers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("text", String),
    Column("date", DateTime),
    Column("user", Integer, ForeignKey("users.id"))
)

# class Parsers(metadata):
#     __tablename__ = "Parsers"
#
#     # Поля таблицы куда будут помещаться распарсенне данные с сайтов
#     id = Column(Integer, primary_key=True, index=True, unique=True)
#     title = Column(String)
#     text = Column(String(350))
#     date = Column(DateTime)
#     user = Column(Integer, ForeignKey("User.id"))
#     user_id = relationship(User)
#
# # без этого не будет работать ассинк. Потому что работа именно
# # c таблицами.
# db_parsers = Parsers.__table__
