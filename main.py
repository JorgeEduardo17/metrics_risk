from fastapi import FastAPI

app = FastAPI()#instancia de fastAPI se crea

@app.get("/")#path operation decorator
def home(): #path operation funtion
    return {"Hello": "World"}