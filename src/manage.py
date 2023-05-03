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


if __name__ == "__main__":
    manager()
