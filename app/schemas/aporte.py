from pydantic import BaseModel
from datetime import date
from typing import Optional

class AporteCreate(BaseModel):
    persona_id: int
    fecha: date
    monto_usdt: float
    tipo_cambio_gtq: float = 7.8
    descripcion: Optional[str] = None

class AporteResponse(BaseModel):
    id: int
    persona_id: int
    fecha: date
    monto_usdt: float
    tipo_cambio_gtq: float
    descripcion: Optional[str]

    class Config:
        from_attributes = True