from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from core.db import metadata
from datetime import datetime, timezone, timedelta
from sqlalchemy.sql import func


parsers = Table("parsers", metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("text", String),
    Column("date", DateTime)
    # Column("user", Integer, ForeignKey("users.id"))
)


# class Parsers(Base):
#     __tablename__ = "parsers"
#
#     # Поля таблицы куда будут помещаться распарсенне данные с сайтов
#     id = Column(Integer, primary_key=True, index=True, unique=True)
#     title = Column(String)
#     text = Column(String)
#     date = Column(DateTime)
#     # user = Column(Integer, ForeignKey("User.id"))
#     # user_id = relationship("Users")
#
# # без этого не будет работать ассинк. Потому что работа именно
# # c таблицами.
# parsers = Parsers.__table__
