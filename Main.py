from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import logging
app = FastAPI()

#Damos de alta cosas de Jinja
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

#Definimos el log
logger = logging.getLogger("foo")

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None
class producto(BaseModel):
    titulo: str
    texto: str
    precio: int

external_data = {
    'titulo': 'Vestido Azul',
    'texto': 'Lindo vestido azul de segunda mano en buenas condiciones',
    'precio': 79.99,
}
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
@app.put("/items/{item_id}")
def create_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}
@app.get("/pag/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
@app.get("/perfil/{cantidad}", response_class=HTMLResponse)
async def read_item(request: Request, cantidad: int):
    return templates.TemplateResponse("hijo.html", {"request": request
                                                    , "cantidad": cantidad
                                                    , "nombre": "Roelver"
                                                    , "subtitulo": "Hola"
                                                    , "texto": "TextoRoelver"
                                                    , "lista": ["apple", "banana", "cherry"]
                                                    , "precio": 777})
@app.put("/ropa/{cantidad}")
async def FuncionTemplateMacro(request: Request):
    logger.warning("Iniciando")
    listaProductos = [producto(**external_data), producto(**external_data)]
    return templates.TemplateResponse("templateMacro.html", {"request": request
                                                            , "productos" : listaProductos
                                                            , "nombre": "Roelver"})