from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from .service import *
from .schemas import PostCreate, PostList
from typing import List

router = APIRouter()


# @router.get("/home", response_model=List[PostList])
# def all_posts_list(db: Session = Depends(get_db)):
#     posts = all_posts(db)
#     return posts


@router.get("/home", response_model=List[PostList])
async def all_posts_list():
    posts = await all_posts()
    return posts


@router.post("/home", response_model=PostList)  #
async def create_appl(item: PostCreate):
    parser = await create_parser(item=item)
    return parser


# @router.get("/home/{post_id}", response_model=List[PostList])
# async def all_posts_list(post_id: int):
#     posts = await all_posts(post_id)
#     return posts


# @router.post("/home")
# def create_post_list(item: PostCreate, db: Session = Depends(get_db)):
#     posts = create_post(item, db)
#     return posts



