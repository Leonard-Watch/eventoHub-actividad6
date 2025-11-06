from __future__ import annotations
from datetime import datetime
from typing import List
from pydantic import BaseModel
from .evento import Paginacion   # re-usamos la misma clase

class ComentarioCrear(BaseModel):
    texto: str

class Comentario(BaseModel):
    id: int
    texto: str
    fecha: datetime

class ComentariosResp(BaseModel):
    meta: Paginacion
    data: List[Comentario]