from .models import *
from .schemas import *
from src.core import database
from datetime import datetime


async def all_menu():
    __menu = await database.fetch_all(restaurant.select())
    return __menu


async def create_dish(item: Dish):

    # Time create dish
    date_now = datetime.now()

    __dish = dish.insert().values(dish_name=item.dish_name,
                                 weight=item.weight,
                                 final_price=item.final_price,
                                 created_on=date_now,
                                 updated_on=date_now
                                 )
    __dish_id = await database.execute(__dish)
    return ShowDish(**item.dict(), id=__dish_id, created_on=date_now)


# async def all_posts(post_id: int):
#     post = await database.fetch_one(db_posts.select().where(db_posts.id == post_id))
#     return post


