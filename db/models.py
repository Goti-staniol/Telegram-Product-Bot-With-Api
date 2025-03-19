from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (
    create_engine,
    Column,
    ForeignKey,
    String,
    Integer,
    Float
)

from data.cfg import DB_URL

engine = create_engine(
    DB_URL,
    echo=True,

)

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    username = Column(String(32), nullable=True)
    amount = Column(Float, default=0.0, nullable=False)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(String(100), nullable=True)
    price = Column(Float, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)


