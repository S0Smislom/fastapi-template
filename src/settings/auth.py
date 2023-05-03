import os
from datetime import timedelta

from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv("JWT_SECRET")
    authjwt_access_token_expires: timedelta = timedelta(minutes=15)
    authjwt_refresh_token_expires: timedelta = timedelta(days=30)


@AuthJWT.load_config
def get_config():
    return Settings()
