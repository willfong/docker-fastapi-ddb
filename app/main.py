from fastapi import FastAPI
from .routers import scores


app = FastAPI()

app.include_router(
    scores.router,
    prefix="/scores",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}