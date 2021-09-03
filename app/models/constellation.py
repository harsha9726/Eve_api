from typing import List

from pydantic import BaseModel


class Position(BaseModel):
    x: float
    y: float
    z: float


class Constellation(BaseModel):
    constellation_id: int
    name: str
    position: Position
    region_id: int
    systems: List[int]
