# hello-rag

Minimal Retrieval-Augmented Generation stack that fits on a CPU-only
laptop (32 GB RAM).

## Stack

| Component | Version | Purpose |
|-----------|---------|---------|
| Qdrant | `latest` | Vector DB |
| llama.cpp | `server` tag | GGUF inference |
| FastAPI | 0.111 | RAG glue |

## Quick start

```bash
# 0. inside ai-upskill/stage01_rag/week1/hello_rag
huggingface-cli download microsoft/Phi-3-mini-4k-instruct-gguf Phi-3-mini-4k-instruct-q4.gguf --local-dir models

docker compose pull          # fetch qdrant + llama images
docker compose up -d --build # build FastAPI and start all services
python ingest.py             # load sample docs (place *.txt in ./data)

curl -X POST localhost:8000/query \
     -H "content-type: application/json" \
     -d '{"question":"What is this repo about?"}'
