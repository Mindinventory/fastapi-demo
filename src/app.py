import time

from fastapi import FastAPI
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

app.include_router(router)
