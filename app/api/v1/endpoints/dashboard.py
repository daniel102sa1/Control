from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db

router = APIRouter()

@router.get("/")
def obtener_dashboard(db: Session = Depends(get_db)):
    resumen = db.execute(text("""
        SELECT * FROM vw_resumen_general
    """)).mappings().first()

    reparto = db.execute(text("""
        SELECT * FROM vw_reparto_ganancia_total
    """)).mappings().all()

    historial = db.execute(text("""
        SELECT *
        FROM vw_registros_resultado
        ORDER BY fecha_hora ASC
    """)).mappings().all()

    grafica_capital = [
        {
            "fecha": str(item["fecha_hora"]),
            "capital_usdt": float(item["capital_usdt"]),
            "capital_gtq": float(item["capital_gtq"])
        }
        for item in historial
    ]

    grafica_ganancias = [
        {
            "fecha": str(item["fecha_hora"]),
            "cambio_usdt": float(item["cambio_usdt"] or 0),
            "cambio_gtq": float(item["cambio_gtq"] or 0),
            "estado": item["estado"]
        }
        for item in historial
    ]

    tarjetas = {
        "capital_actual_usdt": float(resumen["capital_actual_usdt"]),
        "capital_actual_gtq": float(resumen["capital_actual_gtq"]),
        "ganancia_total_usdt": float(resumen["ganancia_total_usdt"]),
        "ganancia_total_gtq": float(resumen["ganancia_total_gtq"]),
        "porcentaje_crecimiento": float(resumen["porcentaje_crecimiento"]),
    }

    return {
        "tarjetas": tarjetas,
        "resumen": resumen,
        "reparto": reparto,
        "historial": historial,
        "grafica_capital": grafica_capital,
        "grafica_ganancias": grafica_ganancias
    }