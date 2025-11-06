from fastapi import FastAPI
from .routers import eventos, asistentes, comentarios

app = FastAPI(
    title="EventHub API",
    description="API RESTful para gestión de eventos (2do Parcial)",
    version="1.0.1",
)

# montar routers
app.include_router(eventos.router)
app.include_router(asistentes.router)
app.include_router(comentarios.router)