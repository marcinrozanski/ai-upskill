from fastapi import FastAPI
from pydantic import BaseModel
import httpx, os
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

QDRANT_URL = os.getenv("QDRANT_URL")
LLM_URL    = os.getenv("LLM_URL")

qdrant  = QdrantClient(url=QDRANT_URL)
embedder = SentenceTransformer("intfloat/e5-small-v2")

app = FastAPI()

class Query(BaseModel):
    question: str
    top_k: int = 3

@app.post("/query")
async def rag(q: Query):
    vec = embedder.encode(q.question).tolist()
    hits = qdrant.search(collection_name="docs",
                         query_vector=vec, limit=q.top_k)
    context = "\n".join([h.payload["text"] for h in hits])

    payload = {
        "model": "local-model",
        "messages": [
            {"role": "system", "content": "You answer using only the context provided."},
            {"role": "user", "content": f"{context}\n---\n{q.question}"}
        ],
        "stream": False,
        "max_tokens": 200
    }
    async with httpx.AsyncClient(timeout=60) as cli:
        resp = await cli.post(LLM_URL, json=payload)
    return {"answer": resp.json()["choices"][0]["message"]["content"]}
