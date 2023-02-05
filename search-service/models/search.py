
from typing import Optional, Any, List
from beanie import Document
from pydantic import BaseModel, EmailStr
import datetime

class Search(Document):
    first_name: str
    last_name: str
    link: str
    params: List
    user_address: str
    is_paid: bool
    date: str
    status: str

    class Config:
        schema_extra = {
            "example": {
                "first_name": "tristan",
                "last_name": "seach_name",
                "link": "http://example.com",
                "params": ['param1', 'param2', 'param3'],
                "is_paid": True,
                "date": "07/05/2022",
                "status": "PROGRESS"
            }
        }
