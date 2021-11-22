from typing import Optional

from fastapi import APIRouter

metric_router = APIRouter()


@metric_router.get("/metrics/isuserknow")
async def metrics_user(
    username: str
):
    result = get_historical_metric_log_for_username(username)
    return result

@metric_router.get("/metrics/isipknown")
async def metrics_ip(
    ip: str
):
    result = get_historical_metric_log_for_ip(ip)
    return result

@metric_router.get("/metrics/failedlogincountlastweek")
async def metrics_count(
):  
    result = get_historical_metric_log_failedlogin()
    return result