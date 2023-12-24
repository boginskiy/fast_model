from fastapi import APIRouter
from .service import *
from .schemas import Restaurant, Dish
from typing import List

router = APIRouter()


@router.get("/restaurant/", response_model=List[Restaurant])  #
async def all_menu_view():
    menu = await all_menu()
    return menu


@router.post("/restaurant/category/dish/", response_model=ShowDish)  #
async def create_dish_view(item: Dish):
    dish = await create_dish(item=item)
    return dish


# Расчетные поля. Вес, стоимость
# Вывод даты в ответе
# Работа с SQLAlchemy