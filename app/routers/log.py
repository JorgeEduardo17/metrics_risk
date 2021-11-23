#Python
from app.models.log import Log
from app.business_logic.extraction_data_log import ExtractionDataLog

#Pydantic
from pydantic.main import BaseModel

#FastAPI
from fastapi import APIRouter, Body

log_router = APIRouter()

class LogIN(BaseModel):
    log_description = str


@log_router.post("/log")
async def create_log(
    log: LogIN = Body(
        ...,
        description="Log recibido para metricas",
        example="20140616 05:42:52 vm5 [4f8a7f94:533e226f]"
    )
):
    """Create Log and update Historical Metrics Values"""

    log_instance = ExtractionDataLog.get_Log_intance(log)
    return log_instance