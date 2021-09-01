from typing import List, Dict

from pydantic import BaseModel


class Constellation(BaseModel):
    constellation_id: int
    name: str
    region_id: int
    systems: List[int]



