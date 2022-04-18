from Clases.Perro import perro
from Clases.Util import printclass
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

class ItemC(BaseModel):
    name: str
    price: float
    is_offer: bool = None
class producto(BaseModel):
    titulo: str
    texto: str
    precio: int
    url: str

external_data = {
    'titulo': 'Toñito',
    'texto': 'Lindo perrito con un pasado oscuro. Invitalo a formar parte de tu familia.',
    'precio': 79.99,
    'url': "https://www.nombresdeperros.eu/wp-content/uploads/2020/12/cachorro-blanco-de-nombre-Toby.jpg"
}

#Función home, para probar los servicios
@app.get("/")
def read_root():
    return {"Hello": "World"}
#Función básica, regresa los datos leídos
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
@app.put("/items/{item_id}")
def create_item(item_id: int, item: ItemC):
    return {"item_price": item.price, "item_id": item_id}
#Muestra una página simple con un texto verde y el número introducido
@app.get("/pag/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
#Muestra una página de perfil. Manda una alerta si se presiona el botón. Practica1.
@app.get("/perfil/{cantidad}", response_class=HTMLResponse)
async def read_item(request: Request, cantidad: int):
    return templates.TemplateResponse("hijo.html", {"request": request
                                                    , "cantidad": cantidad
                                                    , "nombre": "Roelver"
                                                    , "subtitulo": "Hola"
                                                    , "texto": "Cantidad: " + str(cantidad )
                                                    , "lista": ["apple", "banana", "cherry"]
                                                    , "precio": 777})
#Muestra una página de productos
@app.get("/producto/{cantidad}")
async def FuncionTemplateMacro(request: Request):
    logger.warning("Iniciando")
    listaProductos = [producto(**external_data), producto(**external_data)]
    #printclass(producto(**external_data))
    return templates.TemplateResponse("templateMacro.html", {"request": request
                                                            , "productos" : listaProductos
                                                            , "nombre": "Roelver"})