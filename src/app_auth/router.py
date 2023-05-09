from fastapi import APIRouter, status
from fastapi.params import Body, Depends
from fastapi.responses import Response
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import PositiveInt

from settings.auth import AuthJWT, settings
from settings.redis import auth_redis

from .dependencies import (check_jwt_auth_and_return_user_id,
                           check_refresh_jwt_and_return_user_id, oauth2_custom)
from .schemas import RestSignup, RestUser
from .services.auth_service import AuthService
from .services.user_service import UserService

router = APIRouter()


@router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED,
    response_model=RestUser,
)
async def signup(
    data: RestSignup = Body(...),
):
    db_model = await UserService().create(data.username, data.password)
    return await RestUser.from_tortoise_orm(db_model)


@router.post(
    "/login",
    response_model=RestUser,
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    authorize: AuthJWT = Depends(),
):
    db_user = await UserService().get_one(username=form_data.username)
    access_token, refresh_token = await AuthService().login(
        authorize,
        db_user,
        form_data.password,
    )
    authorize.set_access_cookies(access_token)
    authorize.set_refresh_cookies(refresh_token)
    return await RestUser.from_tortoise_orm(db_user)


@router.get(
    "/refresh",
    operation_id="authorize",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def refresh(
    current_user_id: PositiveInt = Depends(check_refresh_jwt_and_return_user_id),
    authorize: AuthJWT = Depends(),
):
    db_user = await UserService().get_by_id(current_user_id)
    access_token, refresh_token = AuthService().create_access_refresh_tokens(
        authorize, db_user
    )
    authorize.set_access_cookies(access_token)
    authorize.set_refresh_cookies(refresh_token)


@router.get(
    "/logout",
    response_class=Response,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def logout(authorize: AuthJWT = Depends(oauth2_custom)):
    # Revoke access token
    authorize.jwt_required()
    jti = authorize.get_raw_jwt()["jti"]
    auth_redis.setex(jti, settings.authjwt_access_token_expires, "true")
    # Revoke refresh token
    try:
        from fastapi_jwt_auth.exceptions import MissingTokenError

        authorize.jwt_refresh_token_required()
        refresh_jti = authorize.get_raw_jwt()["jti"]
        auth_redis.setex(refresh_jti, settings.authjwt_refresh_token_expires, "true")
    except MissingTokenError:
        pass

    authorize.unset_jwt_cookies()


@router.get(
    "/me",
    response_model=RestUser,
)
async def me(
    current_user_id: PositiveInt = Depends(check_jwt_auth_and_return_user_id),
) -> RestUser:
    db_user = await UserService().get_by_id(current_user_id)
    return await RestUser.from_tortoise_orm(db_user)
