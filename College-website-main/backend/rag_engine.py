import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("../data/index.faiss")

with open("../data/notices.json", "r", encoding="utf-8") as f:
    documents = json.load(f)


def search(query):

    query_vector = model.encode([query])

    D, I = index.search(np.array(query_vector), k=3)

    results = [documents[i] for i in I[0]]

    return "\n".join(results)