from typing import List

from pydantic import BaseModel
from .position import Position


class Constellation(BaseModel):
    constellation_id: int
    name: str
    position: Position
    region_id: int
    systems: List[int]
