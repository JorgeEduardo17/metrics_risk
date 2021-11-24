
#FastAPI
from fastapi import FastAPI, responses

#Routers Moduls
from app.routers.log import log_router
from app.routers.metrics import metric_router

app = FastAPI()#instancia de fastAPI se crea

app.include_router(log_router)
app.include_router(metric_router)

HTML_INIT = """
<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Bienvenidos</title>
    </head>
    <body>                        
        <h1>Bienvenidos AppGate</h1>
        <p>
            Hola que tal, soy JORGE EDUARDO QUINTANA y les comparto esta PoC "Metriz Risk", espero sea de su agrado.
        </p>
    </body>    
</html>
"""

@app.get('/')
def index():
    body = HTML_INIT
    return responses.HTMLResponse(content=body)
