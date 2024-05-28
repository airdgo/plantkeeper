from fastapi import APIRouter
from sqlmodel import func, select

from app.api.deps import SessionDep
from app.models import SensorReading, SensorReadingsPublic

router = APIRouter()


@router.get("/", response_model=SensorReadingsPublic)
def read_sensor_readings(session: SessionDep, skip: int = 0, limit: int = 100):
    count_statement = select(func.count()).select_from(SensorReading)
    count = session.exec(count_statement).one()
    statement = select(SensorReading).offset(skip).limit(limit)
    sensor_readings = session.exec(statement).all()

    return SensorReadingsPublic(data=sensor_readings, count=count)
