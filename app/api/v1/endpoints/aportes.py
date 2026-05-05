from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.aporte import Aporte
from app.schemas.aporte import AporteCreate, AporteResponse

router = APIRouter()

@router.post("/", response_model=AporteResponse)
def crear_aporte(data: AporteCreate, db: Session = Depends(get_db)):
    nuevo = Aporte(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=List[AporteResponse])
def listar_aportes(db: Session = Depends(get_db)):
    return db.query(Aporte).order_by(Aporte.fecha.desc(), Aporte.id.desc()).all()