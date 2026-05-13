from fastapi import APIRouter

router = APIRouter(prefix="/devices", tags=["Devices"])


@router.get("/")
def get_devices():

    return [
        {
            "id": 1,
            "name": "Living Room Light",
            "status": True
        },
        {
            "id": 2,
            "name": "Kitchen Fan",
            "status": False
        }
    ]