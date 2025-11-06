from fastapi import APIRouter, Query, Path, HTTPException
from typing import List

# imports relativos
from ..models.asistente import Asistente, AsistenteCrear, AsistenteActualizar, AsistentesResp
from ..models.evento import Paginacion
from ..data.mock import MOCK_ASISTENTES, MOCK_EVENTOS

router = APIRouter(prefix="/v1/eventos", tags=["asistentes"])

def _check_event(event_id: int) -> None:
    if not any(e.id == event_id for e in MOCK_EVENTOS):
        raise HTTPException(404, "Evento no encontrado")

@router.get("/{event_id}/asistentes", response_model=AsistentesResp, summary="6. Listar asistentes")
def listar_asistentes(
    event_id: int = Path(...),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    order: str = Query("asc", regex="^(asc|desc)$"),
):
    _check_event(event_id)
    lista = MOCK_ASISTENTES.get(event_id, [])
    reverse = order == "desc"
    lista = sorted(lista, key=lambda x: x.nombre, reverse=reverse)
    pagina = lista[offset: offset + limit]
    return AsistentesResp(
        meta=Paginacion(total=len(lista), limit=limit, offset=offset),
        data=pagina,
    )

@router.post("/{event_id}/asistentes", status_code=201, response_model=Asistente, summary="7. Registrar asistente")
def registrar_asistente(event_id: int, body: AsistenteCrear):
    _check_event(event_id)
    if event_id not in MOCK_ASISTENTES:
        MOCK_ASISTENTES[event_id] = []
    lista = MOCK_ASISTENTES[event_id]
    nuevo_id = 1 if not lista else max(a.id for a in lista) + 1
    nuevo = Asistente(id=nuevo_id, nombre=body.nombre)
    lista.append(nuevo)
    return nuevo

@router.patch("/{event_id}/asistentes/{asistente_id}", response_model=Asistente, summary="8. Editar asistente")
def editar_asistente(
    event_id: int,
    asistente_id: int,
    body: AsistenteActualizar,
):
    if event_id not in MOCK_ASISTENTES:
        raise HTTPException(404, "Evento no encontrado")
    lista = MOCK_ASISTENTES[event_id]
    asistente = next((a for a in lista if a.id == asistente_id), None)
    if not asistente:
        raise HTTPException(404, "Asistente no encontrado")
    asistente.nombre = body.nombre
    return asistente