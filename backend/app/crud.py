from sqlmodel import Session

from app.models import (
    SensorReading,
    SensorReadingBase,
)


def create_sensor_reading(
    *, session: Session, sensor_reading: SensorReadingBase
) -> SensorReading:
    db_sensor_reading = SensorReading.model_validate(sensor_reading)
    session.add(db_sensor_reading)
    session.commit()
    session.refresh(db_sensor_reading)
    return db_sensor_reading
