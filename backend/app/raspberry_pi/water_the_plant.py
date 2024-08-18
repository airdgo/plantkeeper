from time import sleep, time

from app.models import PlantWateredStatus
from app.raspberry_pi import pump
from app.raspberry_pi.config import (
    DEFAULT_WATERING_SECONDS,
    FULL_SATURATION,
    MOISTURE_THRESHOLD,
    ZERO_SATURATION,
)
from app.raspberry_pi.read_with_spi import read_with_spi

plant_status_messages = {
    "watered": "Plant watered.",
    "not_watered": "Soil moisture is sufficient. No need to water the plant.",
}


def percent_translation(raw_val) -> float:
    per_val = (
        abs((raw_val - ZERO_SATURATION) / (FULL_SATURATION - ZERO_SATURATION)) * 100
    )
    return round(per_val, 3)


def start_watering(duration: int):
    t_end = time() + duration
    pump.turn_on()
    try:
        while time() < t_end:
            sleep(0.1)  # Prevent busy-waiting
    finally:
        pump.turn_off()


def should_water_plant(moisture: int, threshold: int = MOISTURE_THRESHOLD) -> bool:
    return moisture >= threshold


def water_the_plant(seconds: int = DEFAULT_WATERING_SECONDS) -> PlantWateredStatus:
    try:
        moisture = read_with_spi(0)

        if not should_water_plant(moisture):
            return PlantWateredStatus(
                watered=False, message=plant_status_messages["not_watered"]
            )

        start_watering(seconds)
        moisture = read_with_spi(0)
        return PlantWateredStatus(
            watered=True, message=plant_status_messages["watered"]
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        pump.turn_off()
        print("Failed to turn off the pump. Please check the system.")


def read_soil_moisture() -> float:
    moisture = read_with_spi(0)
    return percent_translation(moisture)
