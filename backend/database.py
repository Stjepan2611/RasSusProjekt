from model import Recept

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')


database = client.Recepti # ime baze podataka
collection = database.podaci # ime tablice u bazi


async def fetch_one_recept(title):
    document = await collection.find_one({"title":title})
    return document

async def fetch_all_recepte():
    recepti = [] 
    cursor = collection.find({})
    async for document in cursor:
        recepti.append(Recept(**document))
    return recepti 

async def create_recept(recept):
    document = recept
    result = await collection.insert_one(document)
    return document

async def update_recept(title,autor,desc):
    await collection.update_one({"title": title}, {"$set": {"description": desc}}, {"$set": {"autor": autor}})  #trazim po title a update-am ostalo
    document = await collection.find_one({"title": title})
    return document

async def remove_recept(title):
    await collection.delete_one({"title": title})
    return True