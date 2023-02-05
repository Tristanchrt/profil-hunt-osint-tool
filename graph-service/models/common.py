from typing import Optional, Any
from pydantic import BaseModel


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data"
            }
        }

def response_api(status_code, response_type, description, data):
    return {
        "status_code": status_code,
        "response_type": response_type,
        "description": description,
        "data": data
    }