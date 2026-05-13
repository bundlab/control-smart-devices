from fastapi import FastAPI

from routers import auth
from routers import devices
from routers import sensors
from routers import automation

app = FastAPI(title="Enterprise Smart Home API")

app.include_router(auth.router)
app.include_router(devices.router)
app.include_router(sensors.router)
app.include_router(automation.router)


@app.get("/")
def root():
    return {"message": "Smart Home API Running"}