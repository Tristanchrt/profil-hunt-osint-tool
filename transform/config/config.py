from typing import Optional
from pydantic import BaseSettings

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models.extractor import Extractor


class Settings(BaseSettings):
    consume_topic_name: Optional[str] = None
    producer_topic_name: Optional[str] = None
    broker_url: Optional[str] = None
    DATABASE_URL: Optional[str] = None

    class Config:
        env_file = ".env"
        orm_mode = True
    
    
async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(database=client.get_default_database(),
                    document_models=[Extractor])
    


