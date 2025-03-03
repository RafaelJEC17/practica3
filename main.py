from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir peticiones desde cualquier origen (para la página web)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Contador de visitas
visit_count = {"count": 0}

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API"}

@app.get("/visitas")
def get_visits():
    visit_count["count"] += 1
    return {"visitas": visit_count["count"]}