#Python
from typing import Optional

#Pydantic
from pydantic.main import BaseModel
from pydantic.fields import Field

#FastAPI
from fastapi import APIRouter, Query

#Project
from app.models.log import Log
from app.tests.mock_data import MockDataDb
metric_router = APIRouter()


fake_data_db = MockDataDb.get_query_data_metrics_log()


class LogIN(BaseModel):
    log_inf: str = Field(
        ...
    ) 

@metric_router.get("/metrics/")
async def get_metrics(
    username: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=10,
        title="Username",
        description="This is the User"
        ),
    ip_address: str = Query(
        None,
        title="Ip Address",
        description="This is the ip address"
        )
):
    """Get Log by parameters"""
    import pdb; pdb.set_trace()
    if ip_address:
        result =filter(lambda x: x.ip_address == ip_address, fake_data_db)
        return list(result)
    if  username:
        result =filter(lambda x: x.username == username, fake_data_db)
        return list(result)
    return fake_data_db