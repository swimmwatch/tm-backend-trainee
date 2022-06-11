"""
Counter statistic service entrypoint.
"""
from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import FastAPI, Depends

from services.counter_stat.container import \
    CounterStatisticContainer
from services.counter_stat.dal import CityRepository
from services.counter_stat.schemas.city import City
from services.counter_stat.utils import async_init_db

app = FastAPI()
container = CounterStatisticContainer()


@app.on_event('startup')
async def wire_container():
    container.wire(modules=[__name__])


@app.on_event('startup')
async def init_db():
    await async_init_db(container.db())


@app.get('/cities', response_model=List[City])
@inject
async def get_cities(
    cities_rep: CityRepository = Depends(
        Provide[CounterStatisticContainer.cities_repository]
    )
) -> List[City]:
    cities_records = await cities_rep.get_all()
    return [
        City(
            id=city_record.id,
            name=city_record.name
        )
        for city_record in cities_records
    ]
