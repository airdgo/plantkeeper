# TODO use the sensors from rasspberry
from random import randint

# TODO uncomment the lines when running the code on raspberry
# import spidev

# spi = spidev.SpiDev()
# spi.open(0,0)
# spi.max_speed_hz = 1000000 # 1 MHz

def read_with_spi(channel: int):
  # adc = spi.xfer2([1,(8+channel)<<4,0])
  # data = ((adc[1]&3) << 8) + adc[2]
  data = randint(80, 600)
  return data
