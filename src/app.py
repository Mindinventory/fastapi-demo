import datetime
import os
import uuid
import time

# reading the environment variables
import pytz
from dotenv import load_dotenv
from fastapi_utils.tasks import repeat_every
from fastapi.exceptions import RequestValidationError
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from .routes.route import router


description = """
Fastapi Boilerplate
"""

app = FastAPI(title="Fastapi Demo", description=description)
# app.mount("/static", StaticFiles(directory="src/utils/static"), name="static")

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


@app.get("/")
def root():
    return "Fastapi Demo"

@app.middleware("http")
async def add_process_time_header(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(f'{process_time:0.4f} sec')
    return response


# # validate UUID
# def is_valid_uuid(value):
#     try:
#         uuid.UUID(str(value))
#         return True
#     except ValueError:
#         return False


# # Function for changing validation message which provides by pydentic
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     try:
#         # Get the original 'detail' list of errors
#         details = exc.errors()

#         for error in details:
#             path = request.url.path[1:].split('/')
#             for i in path:
#                 path.remove(i) if i.startswith("v") and i[1].isdigit() else path.remove(i) if is_valid_uuid(str(i)) is True else None
#             path = '_'.join(path)
#             field_name = error["loc"][-1]
#             type_error = error["type"].split('.')[-1]
#             mes = get_message(path, field_name + '_' + type_error)
#             return error_response(mes)
#     except Exception as e:
#         logger.error(f"Internal server error: {e.args}")
#         return error_response(get_message("internal_server", "internal"), 500)

app.include_router(router)
