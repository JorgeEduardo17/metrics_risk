from fastapi import APIRouter
from ..models.log import RiskScoreUser
from fastapi import Body, Query, Path

log_router = APIRouter()


@log_router.post("/log")
async def create_log(log: RiskScoreUser = Body(...)):
    """Create Log and update Historical Metrics Values"""
    return log