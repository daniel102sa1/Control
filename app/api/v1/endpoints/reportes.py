from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db

router = APIRouter()

@router.get("/resumen")
def obtener_resumen(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM vw_resumen_general")).mappings().first()
    return result

@router.get("/reparto")
def obtener_reparto(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM vw_reparto_ganancia_total")).mappings().all()
    return result

@router.get("/historial")
def obtener_historial(db: Session = Depends(get_db)):
    result = db.execute(text("""
        SELECT * 
        FROM vw_registros_resultado
        ORDER BY fecha_hora DESC
    """)).mappings().all()
    return result

@router.get("/")
def obtener_reportes_completos(db: Session = Depends(get_db)):
    resumen = db.execute(text("SELECT * FROM vw_resumen_general")).mappings().first()

    reparto = db.execute(text("""
        SELECT * 
        FROM vw_reparto_ganancia_total
    """)).mappings().all()

    historial = db.execute(text("""
        SELECT * 
        FROM vw_registros_resultado
        ORDER BY fecha_hora DESC
    """)).mappings().all()

    return {
        "resumen": resumen,
        "reparto": reparto,
        "historial": historial
    }