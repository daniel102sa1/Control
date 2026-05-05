from pydantic import BaseModel
from typing import Optional

class PersonaCreate(BaseModel):
    nombre: str
    parentesco: Optional[str] = None
    activo: bool = True

class PersonaResponse(BaseModel):
    id: int
    nombre: str
    parentesco: Optional[str]
    activo: bool

    class Config:
        from_attributes = True