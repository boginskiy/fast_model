from datetime import datetime
from typing import Union
from pydantic import BaseModel


# Dishes
class Dish(BaseModel):
    dish_name: str = "Запеканка"
    weight: float = 0.0
    final_price: float = 0.0


class CreateDish(Dish):
    pass


class ShowDish(Dish):
    id: int
    created_on: datetime


class Category(BaseModel):
    category_name: str = "Завтрак"
    dish: Dish


class Restaurant(BaseModel):
    category: Category
    description: str = "Добавить описание"













# ------------------------
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
