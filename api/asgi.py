from fastapi import FastAPI

from api.user import router as user_router
from api.product import router as product_router


app = FastAPI()


async def start_api() -> None:
    app.include_router(user_router)
    app.include_router(product_router)

    import uvicorn
    config = uvicorn.Config(app, host='127.0.0.1', port=1313)
    server = uvicorn.Server(config)
    await server.serve()