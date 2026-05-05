from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.configuracion import Configuracion
from app.schemas.configuracion import ConfiguracionResponse, ConfiguracionUpdate

router = APIRouter()

# 👉 OBTENER CONFIGURACIÓN
@router.get("/", response_model=list[ConfiguracionResponse])
def obtener_config(db: Session = Depends(get_db)):
    return db.query(Configuracion).all()

# 👉 ACTUALIZAR TIPO DE CAMBIO
@router.put("/tipo-cambio", response_model=ConfiguracionResponse)
def actualizar_tipo_cambio(data: ConfiguracionUpdate, db: Session = Depends(get_db)):
    
    config = db.query(Configuracion).filter(Configuracion.nombre == "TIPO_CAMBIO_GTQ").first()

    if not config:
        raise HTTPException(status_code=404, detail="Configuración no encontrada")

    config.valor = data.valor
    db.commit()
    db.refresh(config)

    return config