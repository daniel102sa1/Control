from sqlalchemy import Column, Integer, Float, Date, String, ForeignKey
from app.db.database import Base
from datetime import date

class Aporte(Base):
    __tablename__ = "aportes"

    id = Column(Integer, primary_key=True, index=True)
    persona_id = Column(Integer, ForeignKey("personas.id"), nullable=False)
    fecha = Column(Date, default=date.today)
    monto_usdt = Column(Float, nullable=False)
    tipo_cambio_gtq = Column(Float, default=7.8)
    descripcion = Column(String, nullable=True)