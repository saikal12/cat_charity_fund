# app/api/routers.py
from fastapi import APIRouter

from app.api.endpoints import user_router, donation_router, charityproject_router

main_router = APIRouter()

main_router.include_router(user_router)
main_router.include_router(donation_router, prefix='/donation', tags=['Donation'])
main_router.include_router(charityproject_router, prefix='/charity_project', tags=['CharityProject'])