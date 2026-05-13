from fastapi import APIRouter

router = APIRouter(prefix="/sensors", tags=["Sensors"])


@router.get("/")
def sensor_data():

    return {
        "temperature": 27,
        "humidity": 65,
        "smoke": False
    }