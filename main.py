from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello World'}

class Numeros(BaseModel):
    numero1: float
    numero2: float

@app.post('/suma')
async def suma(numeros : Numeros):
    return {numeros.numero1 + numeros.numero2}

@app.post('/resta')
async def resta(numeros : Numeros):
    return {numeros.numero1 - numeros.numero2}

@app.post('/multiplicar')
async def multi(numeros : Numeros):
    return {numeros.numero1 * numeros.numero2}

@app.post('/divivir')
async def division(numeros : Numeros):
    return {numeros.numero1 / numeros.numero2}