from typing import Tuple

from fastapi_jwt_auth import AuthJWT

from app_auth.exceptions import UserPermissionError, WrongPasswordError
from app_auth.models import User
from app_auth.services.jwt_service import JWTService
from app_auth.utils import get_password_hash, verify_password


class AuthService:
    async def create(
        self,
        username: str,
        password: str,
        is_staff: bool = False,
        is_superuser: bool = False,
    ) -> User:
        hashed_password = get_password_hash(password)
        defaults = {}
        defaults.update(
            password=hashed_password,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )

        db_user, created = await User.get_or_create(
            username=username,
            defaults=defaults,
        )
        if not created:
            raise UserPermissionError("User already exists")
        return db_user

    async def login(self, authorize: AuthJWT, username: str, password: str):
        db_user = await User.get(username=username)
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
