from tortoise import fields

from core.models import AbstractUserModel, TimestampMixin


class User(AbstractUserModel, TimestampMixin):
    is_staff = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=True)
