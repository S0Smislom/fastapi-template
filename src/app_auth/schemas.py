from pydantic import Field, NonNegativeInt, PositiveInt, root_validator
from tortoise.contrib.pydantic import PydanticModel

from .models import User
from .validators import validate_password


class RestSignup(PydanticModel):
    username: str = Field(..., title="Username")
    password: str = Field(..., title="Password")
    password2: str = Field(..., title="Password again")

    _validate_passowrd = root_validator(allow_reuse=True)(validate_password)


class RestLogin(PydanticModel):
    username: str = Field(..., title="Username")
    password: str = Field(..., title="Password")


class RestToken(PydanticModel):
    access_token: str
    refresh_token: str


class RestUser(PydanticModel):
    id: PositiveInt
    username: str

    class Config:
        orig_model = User
