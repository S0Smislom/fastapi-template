import os
from datetime import timedelta

from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from settings.redis import auth_redis


class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv("JWT_SECRET")
    authjwt_access_token_expires: timedelta = timedelta(minutes=15)
    authjwt_refresh_token_expires: timedelta = timedelta(days=30)
    authjwt_denylist_enabled: bool = True
    authjwt_denylist_token_checks: set = {"access", "refresh"}
    authjwt_token_location: set = {"cookies"}


settings = Settings()


@AuthJWT.token_in_denylist_loader
def check_if_token_in_denylist(decrypted_token):
    # TODO Реализовать использование aioredis
    jti = decrypted_token["jti"]
    entry = auth_redis.get(jti)
    return entry and entry == "true"


@AuthJWT.load_config
def get_config():
    return settings
