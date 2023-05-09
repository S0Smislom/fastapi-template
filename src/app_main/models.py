from tortoise import fields

from core.models import AbstractBaseModel, TimestampMixin


class Category(AbstractBaseModel, TimestampMixin):
    title = fields.CharField(max_length=120)
    description = fields.CharField(max_length=500)

    def __str__(self):
        return f"{self.id}. {self.title}"


class Product(AbstractBaseModel, TimestampMixin):
    title = fields.CharField(max_length=120)
    description = fields.CharField(max_length=500)
    category = fields.ForeignKeyField("models.Category", related_name="products")

    def __str__(self):
        return f"{self.id}. {self.title}"
