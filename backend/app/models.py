from datetime import datetime

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class SensorReadingBase(SQLModel):
    soil_moisture: float
    air_humidity: float
    pressure: float
    temperature: float
    uv_index: float


class SensorReading(SensorReadingBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    timestamp: datetime = Field(default_factory=datetime.now)


class SensorReadingPublic(SensorReadingBase):
    id: int
    timestamp: datetime


class SensorReadingsPublic(SQLModel):
    data: list[SensorReadingPublic]
    count: int


class AmbientalData(BaseModel):
    temperature: float
    pressure: float
    humidity: float


class PlantWateredStatus(BaseModel):
    watered: bool
    message: str
