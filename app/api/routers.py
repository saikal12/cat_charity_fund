# app/api/routers.py
from fastapi import APIRouter

from cat_charity_fund.app.api.endpoints import user_router

main_router = APIRouter()

main_router.include_router(user_router)
