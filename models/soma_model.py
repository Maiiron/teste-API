from pydantic import BaseModel

class SomaRequest(BaseModel):
    a: float
    b: float
