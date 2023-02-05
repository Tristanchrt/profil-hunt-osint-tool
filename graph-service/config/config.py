from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings

from models.graph import Graph
from models.extractor import extractor


class Settings(BaseSettings):
    # database configurations
    DATABASE_URL_LOADED: Optional[str] = None
    DATABASE_URL_DATALAKE: Optional[str] = None
    broker_url: Optional[str] = None
    consume_topic_name: Optional[str] = None
    producer_topic_name: Optional[str] = None

    secret_key: str
    algorithm: str = "HS256"

    class Config:
        env_file = ".env"
        orm_mode = True


async def initiate_database_loaded():
    client = AsyncIOMotorClient(Settings().DATABASE_URL_LOADED)
    await init_beanie(database=client.get_default_database(),
                      document_models=[Graph])
    

async def initiate_database_datalake():
    client = AsyncIOMotorClient(Settings().DATABASE_URL_DATALAKE)
    await init_beanie(database=client.get_default_database(),
                      document_models=[extractor])
