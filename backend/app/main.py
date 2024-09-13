from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from datetime import datetime, time
from typing import Any, no_type_check

import RPi.GPIO as GPIO
import sentry_sdk
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware

from app.api.main import api_router
from app.core.config import settings
from app.events.ambiental import store_ambiental_status
from app.raspberry_pi.water_the_plant import water_the_plant

start_of_day = datetime.combine(datetime.now(), time.min)

jobstores = {"default": MemoryJobStore()}

scheduler = AsyncIOScheduler(jobstores=jobstores, timezone="Europe/Bucharest")


@no_type_check
@scheduler.scheduled_job("interval", hours=1, start_date=start_of_day)
def check_if_needs_water() -> None:
    water_the_plant()


@no_type_check
@scheduler.scheduled_job("interval", hours=1, start_date=start_of_day)
async def store_environment_values() -> None:
    await store_ambiental_status()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[Any, Any]:
    print(f"Lifespan added for: {app}")
    # --- startup ---
    if scheduler.state == 0:
        scheduler.start()
    yield
    # --- shutdown ---
    scheduler.shutdown()
    # clean GPIO pins
    GPIO.cleanup()


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
    lifespan=lifespan,
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
