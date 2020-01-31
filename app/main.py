from fastapi import FastAPI
from .routers import login
from .services import util

app = FastAPI()

app.include_router(
    login.router,
    prefix="/login",
)


@app.get("/")
def read_root():
    util.logger.debug("logging debug")
    util.logger.info("logging info")
    util.logger.warn("logging warning")
    util.logger.error("logging error")
    return {"msg": "Hello, World!"}
