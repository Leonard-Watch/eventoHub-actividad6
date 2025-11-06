from datetime import datetime
from app.models.evento import Evento
from app.models.asistente import Asistente
from app.models.comentario import Comentario

MOCK_EVENTOS: list[Evento] = [
    Evento(id=1, nombre="Conferencia IA", fecha=datetime(2026, 5, 10, 9, 0), ubicacion="Centro Conv."),
    Evento(id=2, nombre="Taller UX", fecha=datetime(2026, 5, 12, 14, 30), ubicacion="Online"),
]

MOCK_ASISTENTES: dict[int, list[Asistente]] = {}
MOCK_COMENTARIOS: dict[int, list[Comentario]] = {}

_NEXT_ID: int = 3