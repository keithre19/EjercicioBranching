from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello World'}

class Contraseña(BaseModel):
    contraseña: str

@app.post('/contraseña')
async def registro(contraseña : Contraseña):
    pw = contraseña.contraseña
    if len(pw) > 8:
        if any(c.islower() for c in pw):
            if any(c.isupper() for c in pw):
                if any(c.isdigit() for c in pw[1:-1]):
                    if any(c in '!@#$' for c in pw[1:-1]):
                        return {'mensaje': 'Contraseña aceptada'}
                    else:       
                        return {'mensaje': 'La contraseña debe contener al menos un caracter especial'}
                else:
                    return {'mensaje': 'La contraseña debe contener al menos un número'}
            else:
                return {'mensaje': 'La contraseña debe contener al menos una letra mayúscula'}
        else:
            return {'mensaje': 'La contraseña debe contener al menos una letra minúscula'}
    else:
        return {'mensaje': 'El tamaño de la contraseña debe ser mayor a 8 caracteres'}

