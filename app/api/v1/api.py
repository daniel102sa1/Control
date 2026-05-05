from fastapi import APIRouter

from app.api.v1.endpoints import (
    personas,
    aportes,
    registros,
    reportes,
    configuracion,
    dashboard
)

router = APIRouter()

# 👤 Personas
router.include_router(personas.router, prefix="/personas", tags=["Personas"])

# 💰 Aportes
router.include_router(aportes.router, prefix="/aportes", tags=["Aportes"])

# 📊 Registros
router.include_router(registros.router, prefix="/registros", tags=["Registros"])

# 📈 Reportes
router.include_router(reportes.router, prefix="/reportes", tags=["Reportes"])

# ⚙️ Configuración
router.include_router(configuracion.router, prefix="/configuracion", tags=["Configuración"])

# 📊 Dashboard
router.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])