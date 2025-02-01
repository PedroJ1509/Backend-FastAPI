from pydantic import BaseModel, Field
from datetime import datetime

class ArticuloAnalisisCosto(BaseModel):
    ArticuloAnalisisCosto_ID: int = Field(default=None)
    Fecha: datetime  = Field(default=datetime.now())
    Articulo_ID: int = Field(default=None)
    TotalCosto: float = Field(default=None)
    CostoUnd: float = Field(default=None)
    Ganancia: float = Field(default=None)
    Estado: bool = Field(default=False)
    Cantidad: int = Field(default=None)
    TotalCostoExist: float = Field(default=None)
    TotalCostoFalt: float = Field(default=None)
