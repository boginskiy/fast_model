from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Table, ForeignKey, Text
from sqlalchemy.sql import func
from src.core import metadata


restaurant = Table("restaurant", metadata,
    Column("id", Integer(), primary_key=True),
    Column("category", String(200), ForeignKey("category.category_name")),
    Column("description", Text(), nullable=False)
)


category = Table("category", metadata,
    Column("id", Integer(), primary_key=True),
    Column("category_name", String(200)),
    Column("dish", String(200), ForeignKey("dish.dish_name")),
)


dish = Table("dish", metadata,
    Column("id", Integer(), primary_key=True),
    Column("dish_name", String(200)),
    Column("weight", Integer()),
    Column("final_price", Integer()),
    Column("created_on", DateTime()),  # default=func.now()
    Column("updated_on", DateTime())
    # Column("composition", ),  # Состав блюда
)
