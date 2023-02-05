from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    consume_topic_name: Optional[str] = None
    producer_topic_name: Optional[str] = None
    broker_url: Optional[str] = None
    
    ACCOUNT_USERNAME: Optional[str] = None
    ACCOUNT_PASSWORD: Optional[str] = None

    class Config:
        env_file = ".env"
        orm_mode = True