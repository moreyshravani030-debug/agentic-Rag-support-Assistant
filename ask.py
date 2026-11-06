import os
import time
import chromadb
from google import genai

client = chromadb.PersistentClient(path="db")
col = client.get_collection("docs")
llm = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def answer(question):
    res = col.query(query_texts=[question], n_results=4)
    chunks = res["documents"][0]
    sources = [m["source"] for m in res["metadatas"][0]]
    context = "\n\n".join(chunks)

    prompt = f"""Answer the question using ONLY the context below.
If the answer is not in the context, say: "I could not find this in the documents."

Context:
{context}

Question: {question}"""

    for attempt in range(8):
        try:
            resp = llm.models.generate_content(model="gemini-3.8-flash", contents=prompt)
            return resp.text, sources
        except Exception as e:
            print(f"Busy, retrying ({attempt + 1}/8)...", str(e)[:50])
            time.sleep(3)
    return "Gemini is busy, try again later.", sources

if __name__ == "__main__":
    q = input("Ask a question: ")
    text, sources = answer(q)
    print("\nAnswer:", text)
    print("Sources:", set(sources))
