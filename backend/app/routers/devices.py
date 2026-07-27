from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.device import Device
from app.schemas.device import DeviceCreate
from app.schemas.device import DeviceResponse
from app.schemas.device import DeviceUpdate

router = APIRouter(
    prefix="/devices",
    tags=["Devices"]
)


@router.get(
    "/",
    response_model=list[DeviceResponse]
)
def get_devices(
    db: Session = Depends(get_db)
):
    return db.query(Device).all()

from fastapi.responses import JSONResponse
@router.post(
    "/",
    response_model=DeviceResponse
)
def create_device(
    payload: DeviceCreate,
    db: Session = Depends(get_db)
):
    device = Device(**payload.model_dump())

    db.add(device)
    db.commit()
    db.refresh(device)

    return device


@router.get(
    "/{device_id}",
    response_model=DeviceResponse
)
def get_device(
    device_id: int,
    db: Session = Depends(get_db)
):
    device = (
        db.query(Device)
        .filter(Device.id == device_id)
        .first()
    )

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    return device


@router.put(
    "/{device_id}",
    response_model=DeviceResponse
)
def update_device(
    device_id: int,
    payload: DeviceUpdate,
    db: Session = Depends(get_db)
):
    device = (
        db.query(Device)
        .filter(Device.id == device_id)
        .first()
    )

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    updates = payload.model_dump(
        exclude_unset=True
    )

    for key, value in updates.items():
        setattr(device, key, value)

    db.commit()
    db.refresh(device)

    return device


@router.delete("/{device_id}")
def delete_device(
    device_id: int,
    db: Session = Depends(get_db)
):
    device = (
        db.query(Device)
        .filter(Device.id == device_id)
        .first()
    )

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    db.delete(device)
    db.commit()

    return {
        "message": "Device deleted"
    }