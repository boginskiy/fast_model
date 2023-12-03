from .models import parsers
from .schemas import PostCreate, PostList
from core.db import database
from datetime import datetime


async def all_posts():
    post = await database.fetch_all(parsers.select())
    return post


async def create_parser(item: PostCreate):
    date_born = datetime.now()
    parser = parsers.insert().values(title=item.title, text=item.text, date=date_born)
    parser_id = await database.execute(parser)
    return PostList(**item.dict(), id=parser_id, date=date_born)


# async def all_posts(post_id: int):
#     post = await database.fetch_one(db_posts.select().where(db_posts.id == post_id))
#     return post

# def create_post(item: PostCreate, db: Session):
#     post = Post(**item.dict())
#     db.add(post)
#     db.commit()
#     db.refresh(post)
#     return post

