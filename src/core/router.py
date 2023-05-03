from fastapi import APIRouter

from app_main.router import router as AppMainRouter

router = APIRouter()

router.include_router(AppMainRouter, prefix="", tags=["Main"])

@router.get('/healthcheck')
async def healthcheck():
    return {'message': 'ok'}