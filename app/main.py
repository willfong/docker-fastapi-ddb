from fastapi import FastAPI, HTTPException
from .routers import login, todo
from .services import util
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse, JSONResponse

app = FastAPI()

# This is only really for serving test files. We would probably serve static
# files from S3 directly.
app.mount("/static", StaticFiles(directory="/app/app/static"), name="static")

app.include_router(login.router, prefix="/login")
app.include_router(todo.router, prefix="/todo")


# Require authentication for all requests
# This doesn't really work yet, but the idea is here
@app.middleware("http")
async def require_authorization(request: Request, call_next):
    response = await call_next(request)
    if request.scope['path'].startswith('/todo'):
        #util.logger.warning(request.headers)
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            util.logger.warning("You need to /login")
            return JSONResponse(content={"msg": "Error logging in..."})
        #util.logger.warning(f"Logged in as: {auth_header}")
    return response


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