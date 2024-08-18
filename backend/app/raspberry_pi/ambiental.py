# TODO use the sensors from rasspberry
import random

# import bme280
# import smbus2
from app.models import AmbientalData

# address = 0x77

# bus = smbus2.SMBus(1)

# calibration_params = bme280.load_calibration_params(bus, address)


def read_ambiental_data() -> AmbientalData:
    # data = bme280.sample(bus, address, calibration_params)

    # return AmbientalData(temperature=data.temperature, pressure=data.pressure, humidity=data.humidity)
    return AmbientalData(
        temperature=random.randint(0, 30),
        pressure=random.randint(1000, 1030),
        humidity=random.uniform(0.1, 0.9),
    )
