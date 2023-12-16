from datetime import datetime
from typing import Union, Any

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    text: str
    date: Union[datetime, None] = datetime.now()

    class Config:
        orm_mode = True


class PostList(PostBase):
    id: int


class PostCreate(PostBase):
    pass
