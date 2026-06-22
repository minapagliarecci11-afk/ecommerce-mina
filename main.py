from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Producto(BaseModel):
    nombre: str
    precio: float
    en_stock: bool
productos = []

@app.get("/productos")
def listar_productos():
    return {"productos": productos}

@app.post("/productos")
def agregar_producto(productos: Producto):
    productos.append(productos)
    return{"mensaje": "Producto agregado", "producto": productos}

@app.put("/productos/{id}")
def actualizar_producto(id: int, nombre: str):
    productos[id] = nombre
    return{"mensaje": "Producto actualizado", "producto": nombre}

@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    eliminado = productos.pop(id)
    return{"mensaje": "Producto eliminado", "producto": eliminado}