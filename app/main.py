from fastapi import FastAPI
from .routers import scores
from .log import logger

app = FastAPI()

app.include_router(
    scores.router,
    prefix="/scores",
)

@app.get("/")
def read_root():
    logger.debug("logging debug")
    logger.info("logging info")
    logger.warn("logging warning")
    logger.error("logging error")
    return {"msg": "Hello, World!"}