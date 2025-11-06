from fastapi import Header, HTTPException
from .config import API_KEY


def verificar_token(x_token: str = Header(...)):
    if x_token != API_KEY:
        raise HTTPException(status_code=401, detail="Token inválido")