import os

import typer
import uvicorn

from settings import config

manager = typer.Typer()


@manager.command("runserver")
def runserver(host: str = "0.0.0.0", port: int = 8000):
    uvicorn.run(
        "core.api:app",
        host=host,
        port=port,
        workers=config.API_WORKERS,
        access_log=config.API_IS_DEBUG,
        reload=True,
    )


@manager.command("createsuperuser")
def createsuperuser():
    pass


@manager.command("startapp")
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


if __name__ == "__main__":
    manager()
