
from fastapi import FastAPI
from .routers import log, metrics

app = FastAPI()#instancia de fastAPI se crea

app.include_router(log.router)
app.include_router(metrics.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


