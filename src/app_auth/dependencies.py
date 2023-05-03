from typing import Optional

from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from pydantic import PositiveInt

from settings.auth import AuthJWT

from .services.jwt_service import JWTService


def check_jwt_auth_and_return_user_id(authorize: AuthJWT = Depends()) -> PositiveInt:
    """Check JWT auth and return user_id if it successfully extracts from JWT"""
    authorize.jwt_required()

    user_id: Optional[PositiveInt] = JWTService.get_user_id_from_jwt(authorize)
    if not user_id:
        raise HTTPException(403, detail="Not authenticated")

    return user_id
