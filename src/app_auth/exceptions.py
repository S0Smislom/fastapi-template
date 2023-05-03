from pydantic.errors import PydanticValueError


class UserPermissionError(ValueError):
    """Base error for access rights"""


class RoleError(ValueError):
    """Base error for role"""


class WrongPasswordError(ValueError):
    """Base error for wrong password"""
