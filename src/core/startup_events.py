from fastapi import FastAPI
from fastapi_admin.app import FastAPIAdmin
from fastapi_admin.providers.login import UsernamePasswordProvider

from app_auth.models import User
from settings.config import BASE_DIR
from settings.redis import admin_redis


async def startup_admin(admin_app: FastAPIAdmin):
    await admin_app.configure(
        template_folders=[f"{BASE_DIR}/core/admin/templates"],
        providers=[UsernamePasswordProvider(admin_model=User)],
        redis=admin_redis,
    )
