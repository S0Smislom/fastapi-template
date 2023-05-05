from typing import Optional

from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from pydantic import PositiveInt
from starlette.status import HTTP_403_FORBIDDEN

from settings.auth import AuthJWT

from .auth import OAuth2Custom
from .services.jwt_service import JWTService

oauth2_custom = OAuth2Custom("/v1/login", scopes=[])


def check_jwt_auth_and_return_user_id(
    authorize: AuthJWT = Depends(oauth2_custom),
) -> PositiveInt:
    authorize.jwt_required()
    user_id: Optional[PositiveInt] = JWTService.get_user_id_from_jwt(authorize)
    if not user_id:
        raise HTTPException(HTTP_403_FORBIDDEN, detail="Not authenticated")
    return user_id


def check_refresh_jwt_and_return_user_id(
    authorize: AuthJWT = Depends(oauth2_custom),
) -> PositiveInt:
    authorize.jwt_refresh_token_required()
    user_id: Optional[PositiveInt] = JWTService.get_user_id_from_jwt(authorize)
    if not user_id:
        raise HTTPException(HTTP_403_FORBIDDEN, defail="Not authenticated")
    return user_id
