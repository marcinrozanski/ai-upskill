"""
Simple ingest script: reads *.txt under ./data, embeds with E5-small,
and upserts into the 'docs' collection in Qdrant.
"""
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
from pathlib import Path

COLL = "docs"
client = QdrantClient(url="http://localhost:6333")
embedder = SentenceTransformer("intfloat/e5-small-v2")

if client.collection_exists(COLL):
    client.delete_collection(COLL)

client.create_collection(
    collection_name=COLL,
    vectors_config=models.VectorParams(size=384,
                                       distance=models.Distance.COSINE)
)

points = []
for idx, file in enumerate(Path("data").glob("*.txt")):
    vec = embedder.encode(file.read_text()).tolist()
    points.append(
        models.PointStruct(id=idx, vector=vec,
                           payload={"path": str(file.name),
                                    "text": file.read_text()[:100]})
    )

client.upsert(COLL, points)
print(f"Ingested {len(points)} documents into collection '{COLL}'.")
