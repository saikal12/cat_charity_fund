from fastapi import FastAPI

from cat_charity_fund.app.api.routers import main_router

app = FastAPI()
app.include_router(main_router)