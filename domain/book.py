from typing import Optional
from pydantic import BaseModel

class Book(BaseModel):
    id: Optional[str] = None
    titulo: str
    autor: str
    ano: int
    preco: float
