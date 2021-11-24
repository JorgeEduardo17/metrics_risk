#Python
from pydantic.fields import Field
from app.models.log import Log
from app.business_logic.extraction_data_log import ExtractionDataLog

#Pydantic
from pydantic.main import BaseModel

#FastAPI
from fastapi import APIRouter, Body

log_router = APIRouter()

class LogIN(BaseModel):
    log_inf: str = Field(
        ...
    ) 


@log_router.post("/log/")
async def create_log(
    log: LogIN,
):
    """Create Log and update Historical Metrics Values"""
    log_instance = ExtractionDataLog.get_Log_intance(log.log_inf)
    return log_instance