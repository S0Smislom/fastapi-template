from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from core.exceptions import register_exception_heandlers
from core.middlewares import add_middlewares
from core.router import router
from settings.db import TORTOISE_ORM

from .admin import app as admin_app


def init():
    app = FastAPI(
        title="Trenera",
        description="",
        version="0",
        docs_url="/docs",
        redoc_url="/redocs",
        openapi_tags=[],
    )

    app.include_router(router, prefix="/v1")

    add_middlewares(app)

    register_tortoise(
        app,
        TORTOISE_ORM,
        generate_schemas=True,
        add_exception_handlers=True,
    )

    register_exception_heandlers(app)

    @app.on_event("startup")
    async def startup_event():
        from .startup_events import startup_admin

        await startup_admin(admin_app)

    @app.on_event("shutdown")
    async def shutdown_event():
        pass

    app.mount("/admin", admin_app)

    return app


app = init()
