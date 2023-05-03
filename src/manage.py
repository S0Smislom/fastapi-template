import typer

from core import commands

manager = typer.Typer()


manager.command("createsuperuser")(commands.createsuperuser)
manager.command("startapp")(commands.startapp)
manager.command("runserver")(commands.runserver)

if __name__ == "__main__":
    manager()
