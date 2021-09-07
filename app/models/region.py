from typing import List, Optional

from fastapi import Form

from pydantic import BaseModel


class Region(BaseModel):
    region_id: int
    description: Optional[str] = Form("")
    name: str
    constellations: List[int]
