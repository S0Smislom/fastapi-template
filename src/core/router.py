from fastapi import APIRouter

from app_auth.router import router as AppAuthRouter
from app_main.router import router as AppMainRouter

router = APIRouter()

router.include_router(AppAuthRouter, prefix="", tags=["Auth V1"])
router.include_router(AppMainRouter, prefix="", tags=["Main V1"])


@router.get("/healthcheck")
async def healthcheck():
    return {"message": "ok"}
