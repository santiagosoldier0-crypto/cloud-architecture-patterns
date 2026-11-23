# 04. Serverless y Docker

**ES.** `lambda_function.py` implementa el contrato de respuesta proxy de Lambda/API Gateway sin SDK; `app.py` es una API FastAPI para empaquetar como contenedor compatible con ECS. Son dos destinos alternativos, no una integración desplegada.

**EN.** `lambda_function.py` implements the Lambda/API Gateway proxy response contract without an SDK. `app.py` is a FastAPI service packaged as an ECS-ready container. These are alternative targets, not a deployed integration.

```mermaid
flowchart LR
  E[Evento] --> L[Handler Lambda]
  C[Cliente] --> D[Contenedor Docker / ECS]
  D --> H[/health]
```

Python 3.12 and pytest: `pytest -q`. Container: `docker build -t cloud-demo .`; `docker run --rm -p 8000:8000 cloud-demo`; visit `http://localhost:8000/health`. Stop with Ctrl+C. No AWS resources are created.

**Observed run (Python 3.14):** Lambda handler test `1 passed`. Docker image/API not built in this run.

**GitHub:** [add repository URL]
