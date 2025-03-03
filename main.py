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

# Función para leer y actualizar el contador de visitas en un archivo
def get_visit_count():
    try:
        with open("visitas.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0  # Si no existe el archivo, comenzamos desde 0

def update_visit_count(count):
    with open("visitas.txt", "w") as file:
        file.write(str(count))

@app.get("/", response_class=HTMLResponse)
def read_root():
    # Enviar el archivo HTML cuando se accede a la raíz
    with open("index.html", "r") as file:
        return file.read()

@app.get("/visitas")
def get_visits():
    visit_count = get_visit_count()  # Obtener el contador actual
    visit_count += 1  # Incrementar el contador
    update_visit_count(visit_count)  # Guardar el nuevo contador
    return {"visitas": visit_count}
