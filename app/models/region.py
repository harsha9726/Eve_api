from typing import List

from pydantic import BaseModel


class Region(BaseModel):
    region_id: int
    description: str
    name: str
    constellations: List[int]
