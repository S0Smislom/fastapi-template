from fastapi.exceptions import HTTPException
from pydantic import PositiveInt
from starlette.status import HTTP_404_NOT_FOUND

from app_auth.exceptions import UserPermissionError
from app_auth.models import User
from app_auth.utils import get_password_hash


class UserService:
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

    async def get_by_id(
        self,
        user_id: PositiveInt,
    ) -> User:
        return await self.get_one(pk=user_id)

    async def get_one(
        self,
        *args,
        **kwargs,
    ) -> User:
        db_model = await User.filter(*args, **kwargs).first()
        if not db_model:
            raise HTTPException(HTTP_404_NOT_FOUND, "User not found")
        return db_model
