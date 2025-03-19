import asyncio

from db.models import engine, Base
from api.asgi import start_api


async def start_project() -> None:
    Base.metadata.create_all(engine)
    await asyncio.create_task(start_api())


if __name__ == '__main__':
    asyncio.run(start_project())