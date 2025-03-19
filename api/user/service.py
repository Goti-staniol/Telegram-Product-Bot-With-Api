from typing import Type

from .schemas import User, UpdateUser
from db.methods import add_user, update_user, get_user, delete_user


async def create_user_in_db(user: User) -> None:
    add_user(user.user_id, user.username)

async def modify_user_in_db(
    user_id: int,
    user: UpdateUser
) -> UpdateUser | None:
    _update_user = update_user(
        user_id=user_id,
        new_username=user.username,
        new_user_id=user.user_id
    )
    if _update_user:
        return user
    return None

async def find_user_in_db(user_id: int) -> User:
    user = get_user(user_id)

    return User(
        user_id=user.user_id,
        username=user.username,
        amount=user.amount
    )

async def delete_user_in_db(user_id: int) -> User | None:
    user = delete_user(user_id)
    if user:
        return User(
            user_id=user.user_id,
            username=user.username,
            amount=user.amount
        )
    return None