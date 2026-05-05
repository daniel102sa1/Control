from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.api import router as api_router

from app.db.database import Base, engine

# 👇 IMPORTAR TODOS LOS MODELOS UNA SOLA VEZ
from app.models import persona, aporte, registro, configuracion

# 👇 CREA TABLAS AUTOMÁTICAMENTE
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

# 👇 RUTAS PRINCIPALES
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}