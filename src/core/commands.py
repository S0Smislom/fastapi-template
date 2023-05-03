import asyncio
import os

import uvicorn
from rich import print as rprint
from tortoise import Tortoise

from app_auth.services.auth_service import AuthService
from app_auth.utils import get_login_and_password
from settings import config
from settings.db import TORTOISE_ORM


def runserver(host: str = "0.0.0.0", port: int = 8000):
    uvicorn.run(
        "core.api:app",
        host=host,
        port=port,
        workers=config.API_WORKERS,
        access_log=config.API_IS_DEBUG,
        reload=True,
    )


def startapp(name: str):
    os.mkdir(name)
    app_files = [
        "constants.py",
        "dependencies.py",
        "exceptions.py",
        "models.py",
        "router.py",
        "schemas.py",
        "service.py",
        "utils.py",
    ]
    for file in app_files:
        with open(f"{name}/{file}", "w"):
            pass


def createsuperuser():
    username, password = get_login_and_password()
    asyncio.run(Tortoise.init(config=TORTOISE_ORM))
    asyncio.run(
        AuthService().create(username, password, is_staff=True, is_superuser=True)
    )
    rprint("[green]Superuser created successfully.[/green]")
