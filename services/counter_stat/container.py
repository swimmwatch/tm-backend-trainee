"""
Counter statistic DI container.
"""
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.wiring import providers

from services.counter_stat.dal import CityRepository
from services.db import AsyncDatabase
from services.db.config import DB_URL


class CounterStatisticContainer(DeclarativeContainer):
    db = providers.Singleton(
        AsyncDatabase,
        db_url=DB_URL
    )
    cities_repository = providers.Factory(
        CityRepository,
        session_factory=db.provided.session
    )
