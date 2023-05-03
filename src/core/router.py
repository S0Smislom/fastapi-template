from fastapi import APIRouter

from app_auth.router import router as AppAuthRouter

router = APIRouter()

router.include_router(AppAuthRouter, prefix="", tags=["Auth V1"])


@router.get("/healthcheck")
async def healthcheck():
    return {"message": "ok"}
