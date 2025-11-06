from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class EventoCrear(BaseModel):
    nombre: str
    fecha: datetime
    ubicacion: str

class EventoActualizar(BaseModel):
    nombre: Optional[str] = None
    fecha: Optional[datetime] = None
    ubicacion: Optional[str] = None

class Evento(BaseModel):
    id: int
    nombre: str
    fecha: datetime
    ubicacion: str

class Paginacion(BaseModel):
    total: int
    limit: int
    offset: int

class EventosResp(BaseModel):
    meta: Paginacion
    data: List[Evento]