from sqlmodel import Session

from app import crud
from app.models import SensorReadingBase


def test_create_sensor_reading(db: Session) -> None:
    soil_moisture = 40
    air_humidity = 50
    pressure = 900
    temperature = 26
    uv_index = 2

    sensor_reading_in = SensorReadingBase(
        soil_moisture=soil_moisture,
        air_humidity=air_humidity,
        pressure=pressure,
        temperature=temperature,
        uv_index=uv_index,
    )

    sensor_reading = crud.create_sensor_reading(
        session=db, sensor_reading=sensor_reading_in
    )
    assert sensor_reading.soil_moisture == soil_moisture
    assert sensor_reading.air_humidity == air_humidity
    assert sensor_reading.pressure == pressure
    assert sensor_reading.temperature == temperature
    assert sensor_reading.uv_index == uv_index
    assert sensor_reading.id
    assert sensor_reading.timestamp
