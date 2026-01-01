import streamlit as st
import requests

def layout():
    st.markdown("# RAG Youtuber")
    st.markdown("Ask a question about the YouTube transcripts")

    text_input = st.text_input(label="Ask a question")

    if st.button("Send") and text_input.strip():
        response = requests.post(
            "http://127.0.0.1:8000/rag/query",
            json={"prompt": text_input},
            timeout=30,
        )
        st.error("Backend error. Check that FastAPI is running and ingestion is done.")
        st.stop()

        data = response.json()
        

        st.markdown("## Question")
        st.write(text_input)

        st.markdown("## Answer")
        st.write(data["answer"])

        st.markdown("## Source")
        st.code(data["filepath"])

if __name__ == "__main__":
    layout()
