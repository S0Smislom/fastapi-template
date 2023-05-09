from fastapi_admin.app import app
from fastapi_admin.resources import Dropdown, Field, Model
from fastapi_admin.widgets import displays, inputs

from .models import Category, Product


class AdminCategory(Model):
    label = "Category"
    model = Category
    fields = [
        "id",
        "title",
        "description",
    ]


class AdminProduct(Model):
    label = "Product"
    model = Product
    fields = [
        "id",
        "title",
        "description",
        "category",
    ]


@app.register
class Content(Dropdown):
    label = "Content"
    icon = "fas fa-bars"
    resources = [AdminCategory, AdminProduct]
