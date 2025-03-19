from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    id: int
    owner_id: int
    name: str
    description: Optional[str]
    price: float


class UpdateProduct(BaseModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]

