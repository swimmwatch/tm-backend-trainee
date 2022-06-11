"""
Counter statistic database models.
"""
from sqlalchemy import Column, Integer, String

from services.db import Base


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
