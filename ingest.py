import os
import chromadb

client = chromadb.PersistentClient(path="db")
col = client.get_or_create_collection("docs")

def chunk(text, size=500, overlap=100):
    parts, start = [], 0
    while start < len(text):
        parts.append(text[start:start + size])
        start += size - overlap
    return parts

ids, docs, metas = [], [], []
for fname in os.listdir("data"):
    if not fname.endswith(".txt"):
        continue
    with open(os.path.join("data", fname), encoding="utf-8") as f:
        text = f.read()
    for i, c in enumerate(chunk(text)):
        ids.append(f"{fname}-{i}")
        docs.append(c)
        metas.append({"source": fname})

col.upsert(ids=ids, documents=docs, metadatas=metas)
print(f"Done: {len(docs)} chunks stored")