from fastapi import APIRouter, Query, Header, HTTPException, Depends
from typing import Optional
from datetime import datetime

from ..models.evento import (
    Evento, EventoCrear, EventoActualizar, EventosResp, Paginacion
)
from ..data.mock import MOCK_EVENTOS, _NEXT_ID
from ..dependencies import verificar_token

router = APIRouter(prefix="/v1/eventos", tags=["eventos"])

@router.get("/", response_model=EventosResp, summary="1. Listar todos los eventos")
def listar_eventos(
    ubicacion: Optional[str] = Query(None, description="Filtrar por ubicación"),
    limit: int = Query(10, ge=1, le=100, description="Máx. eventos a devolver"),
    offset: int = Query(0, ge=0, description="Eventos a omitir"),
    x_token: str = Header(...),
):
    verificar_token(x_token)
    filtrados = [e for e in MOCK_EVENTOS if ubicacion is None or e.ubicacion == ubicacion]
    pagina = filtrados[offset: offset + limit]
    return EventosResp(
        meta=Paginacion(total=len(filtrados), limit=limit, offset=offset),
        data=pagina,
    )

@router.post("/", status_code=201, response_model=Evento, summary="2. Crear nuevo evento")
def crear_evento(body: EventoCrear):
    global _NEXT_ID
    nuevo = Evento(id=_NEXT_ID, nombre=body.nombre, fecha=body.fecha, ubicacion=body.ubicacion)
    MOCK_EVENTOS.append(nuevo)
    _NEXT_ID += 1
    return nuevo

@router.get("/{event_id}", response_model=Evento, summary="3. Detalle de evento")
def obtener_evento(event_id: int):
    evento = next((e for e in MOCK_EVENTOS if e.id == event_id), None)
    if not evento:
        raise HTTPException(404, "Evento no encontrado")
    return evento

@router.patch("/{event_id}", response_model=Evento, summary="4. Actualizar parcialmente evento")
def actualizar_evento(event_id: int, payload: EventoActualizar):
    evento = next((e for e in MOCK_EVENTOS if e.id == event_id), None)
    if not evento:
        raise HTTPException(404, "Evento no encontrado")
    if payload.nombre is not None:
        evento.nombre = payload.nombre
    if payload.fecha is not None:
        evento.fecha = payload.fecha
    if payload.ubicacion is not None:
        evento.ubicacion = payload.ubicacion
    return evento

@router.delete("/{event_id}", status_code=204, summary="5. Eliminar evento")
def eliminar_evento(event_id: int):
    global MOCK_EVENTOS
    evento = next((e for e in MOCK_EVENTOS if e.id == event_id), None)
    if not evento:
        raise HTTPException(404, "Evento no encontrado")
    MOCK_EVENTOS = [e for e in MOCK_EVENTOS if e.id != event_id]