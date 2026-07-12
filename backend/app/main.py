from fastapi import FastAPI

from app.routers import auth
from app.routers import devices
from app.routers import sensors
from app.routers import automation

app = FastAPI(title="Enterprise Smart Home API")

app.include_router(auth.router)
app.include_router(devices.router)
app.include_router(sensors.router)
app.include_router(automation.router)


@app.get("/")
def root():
    return {"message": "Smart Home API Running"}