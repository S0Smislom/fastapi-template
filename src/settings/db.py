import os

DB_URL = os.getenv("DATABASE_URL")

# Tortoise Models
APP_MODELS = [
    "aerich.models",
    "app_auth.models",
    # "app_main.models",
]

TORTOISE_ORM: dict = {
    "connections": {"default": DB_URL},
    "apps": {
        "models": {
            "models": APP_MODELS,
            "connection": "default",
        },
    },
    # "use_tz": False,
    "timezone": "UTC",
}
