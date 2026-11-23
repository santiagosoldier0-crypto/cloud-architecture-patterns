import os
import itertools
import httpx
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()
SERVICES = os.getenv("SERVICES", "http://service-a:8001,http://service-b:8001").split(",")
TOKEN = os.getenv("API_TOKEN", "demo-token")
selection = itertools.cycle(SERVICES)


@app.get("/api/health")
async def route(x_api_key: str | None = Header(default=None)):
    if x_api_key != TOKEN:
        raise HTTPException(status_code=401, detail="unauthorized")
    target = next(selection)
    async with httpx.AsyncClient(timeout=2) as client:
        response = await client.get(f"{target}/health")
    return response.json()
