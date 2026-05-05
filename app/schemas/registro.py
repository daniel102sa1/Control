from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RegistroCreate(BaseModel):
    capital_usdt: float
    tipo_cambio_gtq: float = 7.8
    nota: Optional[str] = None

class RegistroResponse(BaseModel):
    id: int
    fecha_hora: datetime
    capital_usdt: float
    tipo_cambio_gtq: float
    nota: Optional[str]

    class Config:
        from_attributes = True