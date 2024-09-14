from fastapi import APIRouter

from app.api.routes import measurements, watering

api_router = APIRouter()
api_router.include_router(
    measurements.router, prefix="/measurements", tags=["sensor measurements"]
)
api_router.include_router(watering.router, prefix="/watering", tags=["watering"])
