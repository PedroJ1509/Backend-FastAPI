from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None
    name: str = Field(default="New Product", min_length=5, max_length=50)
    price: float = Field(default=0, ge=0, le=1000) # ge = Mahor o igual que, le = Menor o igual que, gt = Mayor que, lt = Menor que
    quantity: int = Field(default=0, gt=0)