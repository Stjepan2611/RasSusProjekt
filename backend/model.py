from pydantic import BaseModel

class Recept(BaseModel):
    title: str
    autor: str
    description: str