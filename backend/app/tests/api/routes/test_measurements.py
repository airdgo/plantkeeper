from fastapi.testclient import TestClient

from app.core.config import settings


def test_read_sensor_measurements(client: TestClient) -> None:
    start_date = "2024-07-31T00:00:00"
    end_date = "2024-08-31T23:59:59"
    skip = 0
    limit = 0
    r = client.get(
        f"{settings.API_V1_STR}/measurements/?start_date={start_date}&end_date={end_date}&skip={skip}&limit={limit}"
    )
    measurements = r.json()
    assert measurements
    assert "data" in measurements
    assert "count" in measurements


def read_sensor_measurements_now(client: TestClient) -> None:
    r = client.get(f"{settings.API_V1_STR}/measurements/now")
    measurement = r.json()
    assert measurement
    assert measurement["soil_moisture"]
    assert measurement["air_humidity"]
    assert measurement["pressure"]
    assert measurement["temperature"]
    assert measurement["uv_index"]
