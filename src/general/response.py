import os
import json
from fastapi.responses import JSONResponse
from .. import logger


def success_response(data, message, code=200, **extra):
    res = {"detail": data,
           "meta": {
               "message": message,
               "code": code,
               **extra
           }
           }
    logger.info(message)
    return res


def error_response(message, code=400):
    res = {
        "message": message,
        "code": code
    }
    return JSONResponse(
        res,
        status_code=code
    )


def nested_error(message, code=400):
    return {"message": message, "code": code}


def get_message(path, data):
    file_path = os.getcwd() + "/src/general/validation_message.json"
    with open(file_path, "r") as file:
        message = json.loads(file.read())
        return message[path][data]
