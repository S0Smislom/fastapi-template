from typing import Tuple

from fastapi_jwt_auth import AuthJWT

from app_auth.exceptions import WrongPasswordError
from app_auth.models import User
from app_auth.services.jwt_service import JWTService
from app_auth.utils import verify_password


class AuthService:
    async def login(self, authorize: AuthJWT, db_user: User, password: str):
        if not verify_password(password, db_user.password):
            raise WrongPasswordError
        access_token, refresh_token = self.create_access_refresh_tokens(
            authorize, db_user
        )
        return access_token, refresh_token

    def create_access_refresh_tokens(
        self, authorize: AuthJWT, db_user: User
    ) -> Tuple[str, str]:
        return JWTService.create_access_refresh_tokens(
            authorize, db_user.username, db_user.pk
        )
