from fastapi import APIRouter, Path, Query, HTTPException, Body
from datetime import datetime

# imports relativos
from ..models.comentario import Comentario, ComentarioCrear, ComentariosResp
from ..models.evento import Paginacion
from ..data.mock import MOCK_COMENTARIOS, MOCK_EVENTOS

router = APIRouter(prefix="/v1/eventos", tags=["comentarios"])

def _check_event(event_id: int) -> None:
    if not any(e.id == event_id for e in MOCK_EVENTOS):
        raise HTTPException(404, "Evento no encontrado")

@router.get("/{event_id}/comentarios", response_model=ComentariosResp, summary="9. Listar comentarios")
def listar_comentarios(
    event_id: int = Path(...),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    _check_event(event_id)
    lista = MOCK_COMENTARIOS.get(event_id, [])
    pagina = lista[offset: offset + limit]
    return ComentariosResp(
        meta=Paginacion(total=len(lista), limit=limit, offset=offset),
        data=pagina,
    )

@router.post("/{event_id}/comentarios", status_code=201, response_model=Comentario, summary="10. Crear comentario")
def crear_comentario(event_id: int, body: ComentarioCrear = Body(...)):
    _check_event(event_id)
    if event_id not in MOCK_COMENTARIOS:
        MOCK_COMENTARIOS[event_id] = []
    lista = MOCK_COMENTARIOS[event_id]
    nuevo_id = 1 if not lista else max(c.id for c in lista) + 1
    nuevo = Comentario(id=nuevo_id, texto=body.texto, fecha=datetime.utcnow())
    lista.append(nuevo)
    return nuevo

@router.delete("/{event_id}/comentarios/{comentario_id}", status_code=204, summary="11. Eliminar comentario")
def eliminar_comentario(
    event_id: int,
    comentario_id: int,
):
    if event_id not in MOCK_COMENTARIOS:
        raise HTTPException(404, "Evento no encontrado")
    lista = MOCK_COMENTARIOS[event_id]
    comentario = next((c for c in lista if c.id == comentario_id), None)
    if not comentario:
        raise HTTPException(404, "Comentario no encontrado")
    MOCK_COMENTARIOS[event_id] = [c for c in lista if c.id != comentario_id]