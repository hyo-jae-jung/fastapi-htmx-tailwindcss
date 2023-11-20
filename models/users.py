from pydantic import BaseModel, EmailStr
from beanie import Document, Link
from typing import Optional, List
from models.events import Event

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Event]]
    class Settings:
        name = "users"
        
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }

class TokenResponse(BaseModel):
    access_token: str
    token_type: str 
