from fastapi import APIRouter

from app.raspberry_pi.water_the_plant import PlantWateredStatus, water_the_plant

router = APIRouter()


@router.post("/water-plant")
def water_plant() -> PlantWateredStatus:
    return water_the_plant()
