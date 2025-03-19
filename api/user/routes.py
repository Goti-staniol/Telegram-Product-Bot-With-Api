from fastapi import APIRouter, HTTPException

from .schemas import User, UpdateUser
from .service import (
    create_user_in_db,
    modify_user_in_db,
    find_user_in_db,
    delete_user_in_db
)


router = APIRouter(tags=['User'])


@router.post('/users/',summary='Add New User',response_model=User)
async def add_user(user: User):
    await create_user_in_db(user)
    return user


@router.get('/users/{user_id}', summary='Get User', response_model=User)
async def get_user(user_id: int):
    user = await find_user_in_db(user_id)
    if user:
        return user
    return HTTPException(404, 'User not found.')


@router.get('/users/all', summary='Get all Users')
async def get_all_user():
    ...


@router.put(
    '/users/{user_id}',
    summary='Update User',
    response_model=UpdateUser)
async def update(user_id: int, update_user: UpdateUser):
    _update_user = await modify_user_in_db(user_id, update_user)
    if _update_user:
        return _update_user
    return HTTPException(404, 'User not found.')


@router.delete('/user/{user_id}', summary='Del User', response_model=User)
async def delete(user_id: int):
    user = await delete_user_in_db(user_id)
    if user:
        return user
    return HTTPException(404, 'User not found.')