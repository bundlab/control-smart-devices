from datetime import datetime
from pydantic import BaseModel


class DeviceCreate(BaseModel):
    name: str
    type: str
    room: str
    topic: str


class DeviceUpdate(BaseModel):
    name: str | None = None
    room: str | None = None
    status: bool | None = None


class DeviceResponse(BaseModel):
    id: int
    name: str
    type: str
    room: str
    topic: str
    status: bool
    created_at: datetime

    class Config:
        from_attributes = True