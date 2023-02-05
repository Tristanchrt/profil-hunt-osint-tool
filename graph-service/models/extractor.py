from beanie import Document

class extractor(Document):
    name: str
    id_search: str
    data: dict
    
    class Config:
        schema_extra = {
            "example": {
                "name": "LINKEDIN",
                "id_search": "user_1234",
                "data": {}
            }
        }
