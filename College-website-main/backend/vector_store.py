import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("../data/notices.json", "r", encoding="utf-8") as f:
    documents = json.load(f)

embeddings = model.encode(documents)

dimension = len(embeddings[0])

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

faiss.write_index(index, "../data/index.faiss")

print("✅ Vector database created")