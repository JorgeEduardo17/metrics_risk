from fastapi import APIRouter
from ..models import Log
from fastapi import Body, Query, Path

router = APIRouter()


@router.post("/log")#path operation decorator
def create_log(log: Log = Body(...)):#un aprametro es obligatorio con el (...)
    return log