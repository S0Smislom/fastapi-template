import os

DB_URL = os.getenv("DB_URL")

# Tortoise Models
APP_MODELS = [
    "aerich.models",
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
    # "use_tz": False,  # надо будет уточнить у фронта, нужно ли ему таймзону передавать
    "timezone": "UTC",
}
