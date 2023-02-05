
from typing import Optional, Any, List
from beanie import Document

class Graph(Document):
    id_research: str
    data: dict

    class Config:
        schema_extra = {
            "example": {
                "data": {},
            }
        }
