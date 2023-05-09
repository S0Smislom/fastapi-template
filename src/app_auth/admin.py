from fastapi_admin.app import app
from fastapi_admin.resources import Field, Model
from fastapi_admin.widgets import displays, inputs

from .models import User


@app.register
class AdminResource(Model):
    label = "User"
    model = User
    icon = "fas fa-user"
    page_pre_title = "User list"
    page_title = "User model"
    fields = [
        "id",
        "username",
        Field(
            name="password",
            label="Password",
            display=displays.InputOnly(),
            input_=inputs.Password(),
        ),
        "created_at",
    ]
