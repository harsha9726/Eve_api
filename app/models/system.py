from typing import List, Optional
from fastapi import Form
from pydantic import BaseModel
from .position import Position


class Planets(BaseModel):
    asteroid_belts: Optional[List[int]] = Form([])
    moons: Optional[List[int]] = Form([])
    planet_id: Optional[int] = Form([])


class System(BaseModel):
    constellation_id: int
    name: str
    planets: Optional[List[Planets]] = Form([])
    position: Position
    security_class: Optional[str] = Form("")
    security_status: float
    star_id: Optional[int] = Form(None)
    stargates: Optional[List[int]] = Form([])
    stations: Optional[List[int]] = Form([])
    system_id: int
