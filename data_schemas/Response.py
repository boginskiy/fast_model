from .Request import Request
from pydantic import BaseModel
from .Application import DpApplication
from .Deals import DpDeals


class Response(BaseModel):
    # Данные с класса Request
    Application: dict
    Deals: dict

    # Дополняем атрибутами, которые должны войти в ответ клиенту
    id: int
