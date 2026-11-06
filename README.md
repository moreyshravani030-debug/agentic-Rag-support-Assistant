# Agentic RAG Support Assistant

A RAG-based assistant that answers questions only from my own documents, and shows which file each answer came from.

## Features
- Documents are split into chunks and stored as embeddings in ChromaDB
- Gemini API generates answers from the retrieved context only
- Says "I could not find this in the documents" when the answer is missing
- Shows the source file for every answer
- Streamlit chat interface

## Tech Stack
Python, ChromaDB, Gemini API, Streamlit

## Setup
1. Create and activate a virtual environment
2. `pip install -r requirements.txt`
3. Create a `.env` file with `GEMINI_API_KEY=your_key`
4. Put your `.txt` files in the `data` folder and run `python ingest.py`
5. Start the app with `streamlit run app.py`

## How it works
1. `ingest.py` reads the files in `data`, chunks them and stores embeddings in ChromaDB
2. `ask.py` retrieves the top 3 relevant chunks for a question
3. The chunks are sent to Gemini with the instruction to answer only from them
4. `app.py` shows the answer and its sourcessss