# cloud-architecture-patterns

Ocho demostraciones académicas mínimas de patrones de arquitectura cloud. Los ejemplos locales no crean infraestructura AWS. Python objetivo: 3.12; en el entorno de edición solo está disponible Python 3.14, por lo que la ejecución registrada abajo verifica el código en 3.14.

| # | Proyecto y objetivo | Ejecución | Carpeta |
|---|---|---|---|
| 1 | Circuit Breaker: CLOSED, OPEN y HALF-OPEN | `python circuit_breaker.py` | [01](01-circuit-breaker/) |
| 2 | Retry: hasta 3 reintentos y backoff exponencial | `python retry_demo.py` | [02](02-retry/) |
| 3 | Timeout: limitar espera ante consulta lenta | `python timeout_demo.py` | [03](03-timeout/) |
| 4 | Handler Lambda y API contenedorizada para ECS | `docker build -t cloud-demo .` | [04](04-serverless-docker/) |
| 5 | Control de acceso, distribución y reverse proxy | `docker compose up --build` | [05](05-api-gateway-load-balancer-reverse-proxy/) |
| 6 | Simular hub y tres redes spoke | `python topology.py` | [06](06-hub-and-spoke/) |
| 7 | App portable y pasos reales de migración a EC2 | `docker build -t lift-demo .` | [07](07-lift-and-shift/) |
| 8 | Acceso SSH privado mediante Bastion | `ssh private` (requiere hosts ya creados) | [08](08-bastion/) |

Cada carpeta contiene su explicación en español e inglés, diagrama Mermaid, pasos y el espacio para agregar el enlace de GitHub. Los proyectos 1–3 y 6 usan pytest; para esos proyectos, desde cada carpeta ejecute `python -m pytest -q`. Los demás comandos y los límites de cada demo están en su README.

No se ha desplegado ningún recurso AWS. El Lift-and-Shift y Bastion documentan pasos reales, pero provisionar EC2, red y almacenamiento requiere autorización explícita y puede generar cargos.

## Evidencia de ejecución

Entorno disponible: Python 3.14.0, pytest 9.2.0, Docker 29.8.2, Compose 5.6.0. No hay Python 3.12 instalado; los tests Python se ejecutaron en 3.14 y deben repetirse con 3.12 para validar esa versión objetivo.

| Proyecto | Resultado registrado |
|---|---|
| 1 Circuit Breaker | `2 passed`; estados CLOSED → OPEN → HALF-OPEN → CLOSED verificados. |
| 2 Retry | `2 passed`; salida: `ok`, `intentos: 3`. |
| 3 Timeout | `2 passed`; salida: `operation exceeded 0.2s`. |
| 4 Lambda | `1 passed`; la imagen Docker no se construyó. |
| 5 Gateway | No ejecutado: Docker daemon no disponible (`docker_engine` pipe missing); FastAPI tampoco está instalado en el Python del host. |
| 6 Hub-and-Spoke | `2 passed`. |
| 7 Lift-and-Shift | No ejecutado todavía. |
| 8 Bastion | No ejecutado: necesita hosts SSH configurados. |

## Enlace del repositorio

GitHub: [agregar URL del repositorio]
