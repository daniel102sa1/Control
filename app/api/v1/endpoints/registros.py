from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.registro import Registro
from app.schemas.registro import RegistroCreate, RegistroResponse
from typing import List

router = APIRouter()

# 👉 CREAR REGISTRO
@router.post("/", response_model=RegistroResponse)
def crear_registro(data: RegistroCreate, db: Session = Depends(get_db)):
    nuevo = Registro(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# 👉 LISTAR REGISTROS
@router.get("/", response_model=List[RegistroResponse])
def listar_registros(db: Session = Depends(get_db)):
    return db.query(Registro).order_by(Registro.fecha_hora.desc()).all()