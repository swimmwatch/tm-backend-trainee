"""
Counter statistic service routers
"""
from fastapi import APIRouter

from services.counter_stat.routers import counter_stat

api_router = APIRouter()
api_router.include_router(counter_stat.router)
