from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    consume_topic_name: Optional[str] = None
    producer_topic_name: Optional[str] = None
    broker_url: Optional[str] = None
    
    ACCOUNT_USERNAME: Optional[str] = None
    ACCOUNT_PASSWORD: Optional[str] = None
    TARGET_LINK: Optional[str] = None
    TARGET_FNAME: Optional[str] = None
    TARGET_NAME: Optional[str] = None
    TARGET_CITY: Optional[str] = None
    TARGET_COMPANY: Optional[str] = None

    class Config:
        env_file = ".env"
        orm_mode = True