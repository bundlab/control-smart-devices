from datetime import datetime
from enum import Enum

from pydantic import BaseModel, field_validator


class DeviceType(str, Enum):
    """Supported device types accepted by the API.

    Inherits from ``str`` so values serialise as plain strings
    (e.g. "Smart Plug"), which is what the database stores.
    """

    LIGHT = "Light"
    SMART_PLUG = "Smart Plug"
    FAN = "Fan"
    THERMOSTAT = "Thermostat"
    CAMERA = "Camera"
    TV = "TV"
    SENSOR = "Sensor"


class DeviceCreate(BaseModel):
    name: str
    type: DeviceType
    room: str
    topic: str


class DeviceUpdate(BaseModel):
    name: str | None = None
    type: DeviceType | None = None
    room: str | None = None
    status: bool | None = None

    @field_validator("type")
    @classmethod
    def type_not_null(cls, value):
        """Reject an explicit null for ``type`` with a clear 422 error."""
        if value is None:
            raise ValueError("type cannot be null")
        return value


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