from fastapi import APIRouter
from fastapi.params import Body, Depends
from fastapi.security import HTTPBearer
from pydantic import PositiveInt
from starlette.status import HTTP_201_CREATED

from settings.auth import AuthJWT

from .dependencies import check_jwt_auth_and_return_user_id
from .schemas import RestLogin, RestSignup, RestToken, RestUser
from .services.auth_service import AuthService

router = APIRouter()


@router.post("/signup", status_code=HTTP_201_CREATED, response_model=RestUser)
async def signup(
    data: RestSignup = Body(...),
):
    db_model = await AuthService().create(data.username, data.password)
    return await RestUser.from_tortoise_orm(db_model)


@router.post("/login", response_model=RestToken)
async def login(
    data: RestLogin = Body(...),
    authorize: AuthJWT = Depends(),
):
    access_token, refresh_token = await AuthService().login(
        authorize,
        data.username,
        data.password,
    )
    return RestToken(access_token=access_token, refresh_token=refresh_token)


@router.get("/test", response_model=PositiveInt, dependencies=[Depends(HTTPBearer())])
async def test(
    current_user_id: PositiveInt = Depends(check_jwt_auth_and_return_user_id),
) -> PositiveInt:
    return current_user_id
