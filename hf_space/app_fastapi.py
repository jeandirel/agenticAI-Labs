from fastapi import FastAPI
from pydantic import BaseModel

from agent_service import handler


app = FastAPI(title="Agentic AI Lab 4 - Production & Safety")


class Query(BaseModel):
    query: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/agent")
def agent(q: Query):
    return handler(q.query)
