from app.raspberry_pi.read_with_spi import read_with_spi


def read_uv() -> float:
  raw_data = read_with_spi(1)
  voltage = raw_data * 3.3 / 1024
  uv_index = voltage/0.1
  return uv_index
