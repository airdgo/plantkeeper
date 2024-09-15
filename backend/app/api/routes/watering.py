from fastapi import APIRouter

from app.models import PlantWateredStatus
from app.raspberry_pi.water_the_plant import water_the_plant

router = APIRouter()


@router.post("/water-plant")
def water_plant() -> PlantWateredStatus:
    return water_the_plant()
