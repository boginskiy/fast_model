# import shutil
# from typing import List
# from fastapi import FastAPI, UploadFile, File, APIRouter, Form, Request as _Request_
# from fastapi.responses import JSONResponse
# from data_schemas.Request import Request
# from data_schemas.Response import Response
# from data_schemas.Request import UploadVideo, User, GetVideo, Message
#
#
# video_router = APIRouter()
#
#
# @video_router.post("/qwe")
# async def root(title: str = Form(...),
#                description: str = Form(...),
#                file: UploadFile = File(...)):
#
#     info = UploadVideo(title=title, description=description)
#
#     with open(f'{file.filename}', "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#
#     return {"file_name": file.filename, "info": info}
#
#
# @video_router.post("/img", status_code=201)
# async def upload_image(files: List[UploadFile] = File(...)):
#     for img in files:
#         with open(f'{img.filename}', "wb") as buffer:
#             shutil.copyfileobj(img.file, buffer)
#
#     return {"file_name": "GOOD"}
#
#
# @video_router.get("/video", response_model=GetVideo,
#                   responses={404: {"models_db": Message}})
# async def get_video():
#     user = {'id': 25, 'name': 'Pipec'}
#     video = {'title': "Test", 'description': 'Description'}
#     info = GetVideo(user=user, video=video)
#     return JSONResponse(status_code=200, content=info.dict())
#
#
# @video_router.get("/test")
# async def get_test(req: Request):
#     return {"msg": 123}
#
#
#
# @video_router.post('/')  # response_model=Response
# async def input_application(payload: _Request_):
#     # Делаем словарь для дальнейшей обработки
#     # data = payload
#     # print(data)
#
#     data = await payload.json()
#
#     print(data)
#
#     # data = Request(**data)
#     # print(data)
#
#     # Обработка данных
#     # result_1 = main_func(data)
#
#     # Перекладываем значения с Request в Response
#     # req_Application = data.get('Application')
#     # req_Antifraud = data.get('Antifraud')
#     # req_Deals = data.get('Deals')
#
#     return await payload.json()
#
#         # (
#         # Response(Application=req_Application,
#         #             Antifraud=req_Antifraud,
#         #             Deals=req_Deals,
#         #             id=666))