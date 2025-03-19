from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command


user_router = Router()

@user_router.message(Command('start'))
async def start_handler(msg: Message):
    ...