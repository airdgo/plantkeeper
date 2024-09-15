from fastapi.testclient import TestClient

from app.core.config import settings


def test_water_plant(client: TestClient) -> None:
    r = client.post(f"{settings.API_V1_STR}/watering/water-plant")
    plant_status = r.json()
    assert "watered" in plant_status, "'watered' key not found in the response"
    assert "message" in plant_status, "'message' key not found in the response"
    if plant_status["watered"]:
        assert plant_status["message"] == "Plant has been watered successfully."
    else:
        assert (
            plant_status["message"]
            == "Soil moisture is sufficient. No need to water the plant."
        )
