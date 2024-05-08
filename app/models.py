# models.py

from pydantic import BaseModel
from typing import Optional

class TodoCreate(BaseModel):
    title: str
    description: Optional[str]

class TodoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
