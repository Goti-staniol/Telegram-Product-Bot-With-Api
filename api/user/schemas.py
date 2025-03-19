from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    username: str
    amount: float = 0.0



class UpdateUser(BaseModel):
    user_id: Optional[int] = None
    username: Optional[str] = None






# class Product(BaseModel):
#     id: int
#     product_name: str = Field
#     product_description: Optional[str]
#     price: float = 0.0