from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"test":"jel radi"}

@app.get("/api/recept")
async def get_recept():
    return 1

@app.get("/api/recept{id}")
async def get_recept_by_id(id):
    return 1

@app.post("/api/recept")
async def post_recept(recept):
    return 1

@app.put("/api/recept{id}")
async def put_recept(id, data):
    return 1
@app.delete("/api/recept{id}")
async def delete_recept(id):
    return 1