from pydantic import BaseModel

class ConfiguracionResponse(BaseModel):
    nombre: str
    valor: float

    class Config:
        from_attributes = True

class ConfiguracionUpdate(BaseModel):
    valor: float