from fastapi import APIRouter

from app.api.routes import items, login, measurements, users, utils, watering

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(
    measurements.router, prefix="/measurements", tags=["sensor measurements"]
)
api_router.include_router(watering.router, prefix="/watering", tags=["watering"])
