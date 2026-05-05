from sqlalchemy import Column, Integer, Float, DateTime, String
from app.db.database import Base
from datetime import datetime

class Registro(Base):
    __tablename__ = "registros_capital"

    id = Column(Integer, primary_key=True, index=True)
    fecha_hora = Column(DateTime, default=datetime.utcnow)
    capital_usdt = Column(Float, nullable=False)
    tipo_cambio_gtq = Column(Float, default=7.8)
    nota = Column(String, nullable=True)