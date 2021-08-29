from typing import List

from pydantic import BaseModel


class Constellation(BaseModel):
    constellation_id: int
    name: str
    position: List[float]
    region_id: int
    systems: List[int]



