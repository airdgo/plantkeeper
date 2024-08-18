import logging
from datetime import datetime

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import func, select

from app.api.deps import SessionDep
from app.models import (
    SensorReading,
    SensorReadingBase,
    SensorReadingsPublic,
)
from app.raspberry_pi.ambiental import read_ambiental_data
from app.raspberry_pi.uv import read_uv
from app.raspberry_pi.water_the_plant import read_soil_moisture

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=SensorReadingsPublic)
def read_sensor_measurements(
    session: SessionDep,
    start_date: datetime | None = Query(None, example="2024-07-31T00:00:00"),
    end_date: datetime | None = Query(None, example="2024-08-31T23:59:59"),
    skip: int = 0,
    limit: int = 100,
) -> SensorReadingsPublic:
    if start_date is None or end_date is None:
        raise HTTPException(
            status_code=400,
            detail="Missing 'start_date' or 'end_date'.",
        )

    if end_date < start_date:
        logger.error(
            "Invalid date range specified. Ensure the start date is before the end date."
        )
        raise HTTPException(
            status_code=400,
            detail="Invalid date range specified. Start date must be before end date.",
        )

    count_statement = (
        select(func.count())
        .select_from(SensorReading)
        .where(
            SensorReading.timestamp >= start_date,
            SensorReading.timestamp <= end_date,
        )
    )
    count = session.exec(count_statement).one()
    statement = (
        select(SensorReading)
        .where(
            SensorReading.timestamp >= start_date,
            SensorReading.timestamp <= end_date,
        )
        .offset(skip)
        .limit(limit)
    )
    sensor_readings = session.exec(statement).all()

    return SensorReadingsPublic(data=sensor_readings, count=count)


@router.get("/now", response_model=SensorReadingBase)
def read_sensor_Measurements_now() -> SensorReadingBase:
    soil_moisture = read_soil_moisture()
    ambiental_data = read_ambiental_data()
    uv = read_uv()

    return SensorReadingBase(
        soil_moisture=soil_moisture,
        air_humidity=ambiental_data.humidity,
        pressure=ambiental_data.pressure,
        temperature=ambiental_data.temperature,
        uv_index=uv,
    )
