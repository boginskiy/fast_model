from data_schemas.Request import Request


def main_func(data: Request):
    if data.Application.Phone == "ss":
        data.Application.Phone = "79806397914"
        return data.Application.Phone
    return data
