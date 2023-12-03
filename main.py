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



# Это для несинхронного кода.
# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next: object) -> object:
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response

app.include_router(routers)