from fastapi import FastAPI
from routers import routers
from starlette.responses import Response
from starlette.requests import Request

from core.db import database, engine, metadata

metadata.create_all(bind=engine)
app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(routers)