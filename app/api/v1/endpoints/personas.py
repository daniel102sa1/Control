from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.persona import Persona
from app.schemas.persona import PersonaCreate, PersonaResponse

router = APIRouter()

@router.post("/", response_model=PersonaResponse)
def crear_persona(data: PersonaCreate, db: Session = Depends(get_db)):
    nueva = Persona(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.get("/", response_model=List[PersonaResponse])
def listar_personas(db: Session = Depends(get_db)):
    return db.query(Persona).order_by(Persona.id.asc()).all()