from __future__ import annotations
from pydantic import BaseModel
from typing import List

class AsistenteCrear(BaseModel):
    nombre: str

class AsistenteActualizar(BaseModel):
    nombre: str

class Asistente(BaseModel):
    id: int
    nombre: str

class AsistentesResp(BaseModel):
    data: List[Asistente]