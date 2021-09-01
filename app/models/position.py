from pydantic import BaseModel

class Position(BaseModel):
    x: float
    y: float
    z: float
    object_id: int
    object_type: str