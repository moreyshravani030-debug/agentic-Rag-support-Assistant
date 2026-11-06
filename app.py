import streamlit as st
from ask import answer

st.title("Agentic RAG Support Assistant")
st.caption("Ask questions about your documents. Answers come only from the indexed files.")

q = st.text_input("Your question")
if q:
    with st.spinner("Searching documents..."):
        text, sources = answer(q)
    st.write(text)
    st.caption("Sources: " + ", ".join(sorted(set(sources))))
