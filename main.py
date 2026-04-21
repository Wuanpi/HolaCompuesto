from fastapi import FastAPI
from fastapi.responses import FileResponse

# 1. Creamos una "instancia" de FastAPI
app = FastAPI()

# 2. Definimos una operación de ruta (path operation)
@app.get("/")
def read_index():
    return FileResponse("index.html")

@app.get("/api/datos")
def get_data():
    return {"mensaje": "Hola Mundo"
            , "autor": "Juan Manuel Rondon Gomez"
            , "fecha": "2024-04-21"}
