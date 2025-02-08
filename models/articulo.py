from pydantic import BaseModel, Field

class Articulo(BaseModel):
    Articulo_ID: int = Field(default=None)
    Articulo_CD: str = Field(default="00000", min_length=1, max_length=50)
    Articulo_Desc: str = Field(default="", min_length=1, max_length=80)
    Costo: float = Field(default=0.0)
