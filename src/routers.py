from fastapi import APIRouter
from src.fast_model import fast

routers = APIRouter()

routers.include_router(fast.router, prefix="/v1")

