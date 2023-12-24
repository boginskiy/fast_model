from datetime import datetime


# users = Table(
#     "users",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("email", String, unique=True, index=True),
#     Column("hashed_password", String),
#     Column("is_active", Boolean, default=True)
# )
#
#
# items = Table(
#     "items",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("title", String, index=True),
#     Column("description", String),
#     Column("owner_id", Integer, ForeignKey("users.id"))
# )

# class Users(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True, index=True, unique=True)
#     name = Column(String, unique=True)
#     email = Column(String, unique=True)
#     password = Column(String)
#     date = Column(DateTime)
#     is_active = Column(Boolean, default=False)
#     is_admin = Column(Boolean, default=False)
#
# # без этого не будет работать ассинк. Потому что работа именно
# # c таблицами.
# users = Users.__table__
