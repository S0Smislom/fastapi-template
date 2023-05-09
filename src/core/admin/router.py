from fastapi import Depends
from fastapi_admin.app import app as admin_app
from fastapi_admin.depends import get_current_admin, get_resources
from fastapi_admin.template import templates
from starlette.requests import Request


@admin_app.get("/", dependencies=[Depends(get_current_admin)])
async def home(request: Request, resources=Depends(get_resources)):
    return templates.TemplateResponse(
        name="home.html",
        context={
            "request": request,
            "resources": resources,
            "resource_label": "Home",
            "page_pre_title": "overview",
            "page_title": "Home",
        },
    )
