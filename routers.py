from fastapi import APIRouter
from fast_model import fast


routers = APIRouter()

routers.include_router(fast.router, prefix="/v1")

