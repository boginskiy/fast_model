from datetime import datetime
from typing import Union, Any

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    text: str
    # date: datetime = datetime.now()

    class Config:
        orm_mode = True


class PostList(PostBase):
    id: int
    date: datetime


class PostCreate(PostBase):
    pass


