import os
from fastapi import FastAPI

app = FastAPI()
SERVICE_NAME = os.getenv("SERVICE_NAME", "service")


@app.get("/health")
def health():
    return {"service": SERVICE_NAME}
