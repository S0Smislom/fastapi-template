from typing import Dict, Optional, Tuple, Union

from pydantic import PositiveInt

from settings.auth import AuthJWT


class JWTService:
    # TODO add token revoke

    @staticmethod
    def create_access_refresh_tokens(
        authorize: AuthJWT,
        username: str,
        user_id: Optional[PositiveInt] = None,
    ) -> Tuple[str, str]:
        user_claims = {}
        if user_id:
            user_claims.update(user_id=user_id)

        access_token = authorize.create_access_token(
            subject=username, user_claims=user_claims
        )
        refresh_token = authorize.create_refresh_token(
            subject=username,
            user_claims=user_claims,
        )
        return access_token, refresh_token

    @staticmethod
    def create_access_token(
        authorize: AuthJWT,
        username: str,
        user_id: Optional[PositiveInt] = None,
    ) -> str:
        user_claims = {}
        if user_id:
            user_claims.update(user_id=user_id)

        return authorize.create_access_token(
            subject=username,
            user_claims=user_claims,
        )

    @staticmethod
    def get_user_id_from_jwt(authorize: AuthJWT) -> Optional[PositiveInt]:
        raw_jwt: Optional[Dict[str, Union[str, int, bool]]] = authorize.get_raw_jwt()
        if not raw_jwt:
            return
        user_id = raw_jwt.get("user_id")
        if user_id:
            user_id = int(user_id)
        return user_id
