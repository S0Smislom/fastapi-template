from tortoise import fields, models


class AbstractModel(models.Model):
    class Meta:
        abstract = True


class TimestampMixin(AbstractModel):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class PublishedModel(AbstractModel):
    published = fields.BooleanField(default=True, description="Опубликовано?")


class AbstractBaseModel(AbstractModel):
    id = fields.IntField(pk=True)


class AbstractUserModel(AbstractModel):
    username = fields.CharField(max_length=120)
    password = fields.CharField(max_length=200)
