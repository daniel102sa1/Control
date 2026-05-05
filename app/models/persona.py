from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base

class Persona(Base):
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    parentesco = Column(String, nullable=True)
    activo = Column(Boolean, default=True)