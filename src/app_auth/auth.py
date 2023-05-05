from fastapi.requests import Request
from fastapi.responses import Response
from fastapi.security import OAuth2PasswordBearer

from settings.auth import AuthJWT


class OAuth2Custom(OAuth2PasswordBearer):
    async def __call__(self, request: Request = None, response: Response = None):
        return AuthJWT(request, response)
