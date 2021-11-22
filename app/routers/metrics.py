from fastapi import APIRouter

router = APIRouter()


@router.get("/metrics/detail")
def show_person(
):
    return {}