from typing import Tuple

import typer
from passlib.context import CryptContext
from rich import print as rprint

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_login() -> str:
    login = typer.prompt("Username")
    return login


def get_password() -> str:
    password = typer.prompt("Password", hide_input=True)
    password_again = typer.prompt("Password (again)", hide_input=True)
    if password_again != password:
        rprint("[red]Passwords not equal.[/red]")
        raise typer.Abort()
    return password


def get_login_and_password() -> Tuple[str, str]:
    login = get_login()
    password = get_password()
    return login, password
