from pydantic import BaseModel
     

class Recept(BaseModel):
    title: str
    description: str
    autor: str
