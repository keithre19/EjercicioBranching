from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Texto(BaseModel):
    cadena: str

@app.post('/analizar')
async def analizar_texto(texto: Texto):
    cadena = texto.cadena
    cantidad_letras = sum(c.isalpha() for c in cadena)
    cantidad_vocales = sum(c.lower() in 'aeiou' for c in cadena)
    cantidad_numeros = sum(c.isdigit() for c in cadena)
    cantidad_espacios = sum(c.isspace() for c in cadena)

    return {
        "cantidad_letras": cantidad_letras,
        "cantidad_vocales": cantidad_vocales,
        "cantidad_numeros": cantidad_numeros,
        "cantidad_espacios": cantidad_espacios
    }