from fastapi import FastAPI
from data_schemas.Request import Request
from data_schemas.Response import Response

app = FastAPI()


@app.post('/', response_model=Response)
def input_application(payload: Request):
    # Делаем словарь для дальнейшей обработки
    data = payload.dict()

    # Обработка данных
    # result_1 = main_func(data)

    # Перекладываем значения с Request в Response
    req_Application = data.get('Application')
    req_Deals = data.get('Deals')

    return Response(Application=req_Application,
                    Deals=req_Deals,
                    id=777)
