from typing import Optional, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()
products = []


class Product(BaseModel):
    id: int
    name: str
    desc: Optional[str]
    price: float
    is_buy: bool = False


@app.post('/products/', response_model=Product)
async def add_product(product: Product):
    products.append(product)
    return product


@app.get('/products/', response_model=List[Product])
async def read_products():
    return products


@app.put('/products/{product_id}', response_model=Product)
async def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product

    raise HTTPException(status_code=404, detail='Product Not Found')


@app.delete('/product/{product_id}', response_model=Product)
async def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            deleted_product = products.pop(index)
            return deleted_product

    raise HTTPException(status_code=404, detail='Product Not Found')

