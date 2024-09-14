import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlmodel import Session

from app.api.deps import get_db
from app.crud import create_sensor_reading
from app.models import SensorReadingBase
from app.raspberry_pi.ambiental import read_ambiental_data
from app.raspberry_pi.uv import read_uv
from app.raspberry_pi.water_the_plant import read_soil_moisture

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan_context() -> AsyncGenerator[Session, None]:
    session_generator = get_db()
    try:
        session = next(session_generator)
        yield session
    finally:
        session_generator.close()


def gather_sensor_data() -> SensorReadingBase:
    soil_moisture = read_soil_moisture()
    ambiental_data = read_ambiental_data()
    uv_index = read_uv()
    sensor_reading = SensorReadingBase(
        soil_moisture=soil_moisture,
        air_humidity=ambiental_data.humidity,
        pressure=ambiental_data.pressure,
        temperature=ambiental_data.temperature,
        uv_index=uv_index,
    )
    logger.info(f"Sensor data gathered: {sensor_reading}")
    return sensor_reading


def store_reading(session: Session, sensor_reading: SensorReadingBase) -> None:
    try:
        create_sensor_reading(session=session, sensor_reading=sensor_reading)
        logger.info("Sensor reading stored successfully")
    except Exception as e:
        logger.error(f"Failed to store sensor reading: {e}")
        raise e


async def store_ambiental_status() -> None:
    logger.info("Starting environment status storage task")
    async with lifespan_context() as session:
        try:
            sensor_reading = gather_sensor_data()
            store_reading(session, sensor_reading)
            logger.info("Environment status stored successfully")
        except Exception as e:
            logger.error(f"Error in store_ambiental_status: {e}")
