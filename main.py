from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Conexión a MongoDB Atlas
@app.on_event("startup")
async def startup_db_client():
    # Aquí debes colocar la URL de conexión de MongoDB Atlas
    mongo_uri =  client = "mongodb+srv://Rafael:12345@cluster0.4bqxv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    app.mongodb_client = AsyncIOMotorClient(mongo_uri)
    app.mongodb = app.mongodb_client["mi_base_de_datos"]  # Reemplaza "mi_base_de_datos" con el nombre que elegiste

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

# Middleware CORS (permite solicitudes desde cualquier origen)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Contador de visitas
@app.get("/visitas")
async def get_visits():
    visits_collection = app.mongodb["visitas"]  # Colección donde se guardarán las visitas
    visit = await visits_collection.find_one({"_id": "contador"})
    
    if not visit:
        # Si no existe el contador, se crea con valor 1
        visit = {"_id": "contador", "count": 1}
        await visits_collection.insert_one(visit)
    else:
        # Si existe, incrementa el contador
        visit["count"] += 1
        await visits_collection.update_one({"_id": "contador"}, {"$set": {"count": visit["count"]}})
    
    return {"visitas": visit["count"]}
