from pydantic import BaseModel, Field

class IncrementoPrecioRequest(BaseModel):
    porcentaje: float = Field(default=0.0)
    tokenFirebase: str = Field(default="")
