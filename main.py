from fastapi import FastAPI
from src.routers import routers
from src.core import database, engine, metadata


metadata.create_all(bind=engine)
app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(routers)
