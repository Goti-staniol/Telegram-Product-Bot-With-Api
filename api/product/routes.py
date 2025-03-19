from fastapi import APIRouter, HTTPException

from .schemas import Product, UpdateProduct


router = APIRouter(tags=['Product'])


@router.post(
    '/product/',
    summary='Add product',
    response_model=Product)
async def add_product():
    ...


@router.get(
    '/products/{id}',
    summary='Get Product',
    response_model=Product)
async def get_product():
    return


