from fastapi import FastAPI
from .routers import login
from .services import util
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

app = FastAPI()

# This is only really for serving test files. We would probably serve static
# files from S3 directly.
app.mount("/static", StaticFiles(directory="/app/app/static"), name="static")

app.include_router(
    login.router,
    prefix="/login",
)


@app.get("/")
def index():
    return RedirectResponse(url='/static/index.html')


@app.get("/log-output-test")
def log_output_test():
    util.logger.debug("logging debug")
    util.logger.info("logging info")
    util.logger.warn("logging warning")
    util.logger.error("logging error")
    return {"msg": "Logging output"}