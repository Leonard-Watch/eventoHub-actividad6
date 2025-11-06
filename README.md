# EventHub API

API RESTful de gestión de eventos, asistentes y comentarios.  
Proyecto correspondiente al **2do Parcial** de *Técnicas Avanzadas de Programación* – ISET 2025.



## Stack
- Python 3.12+
- FastAPI
- Uvicorn



## 1. Instalación

1. **Descomprimir / clonar** el repo en una carpeta local.
2. Abrir una terminal **dentro de la carpeta raíz** ("eventoapi"). 


## 2. Instalación dependencia 

1. pip install -r requirements.txt

- Si no existe requirements.txt, instalar manualmente:
 * pip install fastapi uvicorn

## 3. Ejecutar 

1. Opción corta: **python run.py**
2. Opción larga: **python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000**


## 4. Token de seguridad
Solo probado en eventos listar:
x-token: 12345