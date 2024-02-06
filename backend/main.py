from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import (
    fetch_one_recept,
    fetch_all_recepte,
    create_recept,
    update_recept,
    remove_recept,
)

from model import Recept

app = FastAPI()



@app.get("/")
def read_root():
    return {"test":"jel radi"}

@app.get("/api/recept")
async def get_recept():
    response = await fetch_all_recepte()
    return response

@app.get("/api/recept{title}", response_model=Recept)
async def get_recept_by_id(title):
    response = await fetch_one_recept(title)
    if response:
        return response
    raise HTTPException(404, f"nema recepta pod ovim imenom {title}")

@app.post("/api/recept", response_model=Recept)
async def post_recept(recept:Recept):
    response = await create_recept(recept.dict())
    if response:
        return response
    raise HTTPException(400, "no work")
    

@app.put("/api/recept{title}/", response_model=Recept)
async def put_recept(title:str, autor:str, desc:str):
    response = await update_recept(title,autor,desc)
    if response:
        return response
    raise HTTPException(404, f"nema recepta pod ovim imenom {title}")

@app.delete("/api/recept{title}")
async def delete_recept(title):
    response = await remove_recept(title)
    if response:
        return "Obrisano"
    raise HTTPException(404, f"nema recepta pod ovim imenom {title}")