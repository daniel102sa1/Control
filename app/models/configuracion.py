from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class Configuracion(Base):
    __tablename__ = "configuracion"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)
    valor = Column(Float, nullable=False)