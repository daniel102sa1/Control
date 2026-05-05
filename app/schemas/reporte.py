from pydantic import BaseModel
from typing import Optional

class ResumenGeneralResponse(BaseModel):
    capital_inicial_usdt: float
    capital_inicial_gtq: float
    capital_actual_usdt: float
    capital_actual_gtq: float
    ganancia_total_usdt: float
    ganancia_total_gtq: float
    porcentaje_crecimiento: float

class RepartoResponse(BaseModel):
    persona_id: int
    nombre: str
    aporte_usdt: float
    aporte_gtq: float
    porcentaje_participacion: float
    resultado_persona_usdt: float
    resultado_persona_gtq: float
    estado: str

class HistorialResponse(BaseModel):
    id: int
    fecha_hora: str
    capital_usdt: float
    capital_gtq: float
    tipo_cambio_gtq: float
    capital_anterior_usdt: Optional[float]
    cambio_usdt: Optional[float]
    cambio_gtq: Optional[float]
    estado: str
    porcentaje_cambio: Optional[float]