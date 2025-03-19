from typing import Type

from sqlalchemy.orm import sessionmaker

from db.models import User, Product
from db.models import engine


Session = sessionmaker(bind=engine)


def add_user(user_id: int, username: str) -> None:
    with Session() as session:
        user = session.query(User).filter_by(user_id=user_id).first()

        if not user:
            new_user = User(
                user_id=user_id,
                username=username
            )
            session.add(new_user)
            session.commit()

def update_user(
    user_id: int,
    new_username: str | None = None,
    new_user_id: str | None = None
) -> bool | None:
    with Session() as session:
        user = session.query(User).filter_by(user_id=user_id).first()
        if user:
            if new_user_id:
                user.user_id = new_user_id
            if new_username:
                user.username = new_username
            session.commit()
            return True
        return None

def get_user(user_id: int) -> Type[User] | None:
    with Session() as session:
        user = session.query(User).filter_by(user_id=user_id).first()
        if user:
            return user
        return None

def all_user_from_db() -> dict:
    with Session() as session:
        users = session.query(User).all()
        data = {
            user.id: {
                'user_id': user.user_id,
                'username': user.username,
                'amount': user.amount
            }
            for user in users
        }
        return data

def delete_user(user_id: int) -> Type[User] | None:
    with Session() as session:
        user = get_user(user_id)
        if user:
            session.delete(user)
            session.commit()
            return user
        return None

def add_product(
    owner_id: int,
    product_id: int,
    product_name: str,
    product_description: str | None,
    product_price: float
) -> None:
    with Session() as session:
        product = get_product(product_id)
        if not product:
            new_product = Product(
                id=product_id,
                name=product_name,
                product_description=product_description,
                price=product_price,
                owner_id=owner_id
            )
            session.add(new_product)
            session.commit()

def get_product(product_id: int) -> Type[Product] | None:
    with Session() as session:
        product = session.query(Product).filter_by(
            product_id=product_id
        ).first()

        if product:
            return product
        return None

def update_product(
    product_id: int,
    new_product_name: str | None,
    new_product_description: str | None,
    new_price: str | None
) -> None:
    with Session() as session:
        ...



