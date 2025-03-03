from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir peticiones desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Contador de visitas
visit_count = {"count": 0}

@app.get("/", response_class=HTMLResponse)
def read_root():
    # Enviar el archivo HTML cuando se accede a la raíz
    with open("index.html", "r") as file:
        return file.read()

@app.get("/visitas")
def get_visits():
    visit_count["count"] += 1
    return {"visitas": visit_count["count"]}
