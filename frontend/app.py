import streamlit as st
import requests
from pathlib import Path


st.set_page_config(
    page_title="RAG YouTuber Assistant",
    page_icon="📚",
    layout="wide",
)

ASSETS_PATH = Path(__file__).parents[1] / "assets"


def layout():
    
    st.image(ASSETS_PATH / "abdulrahman.png", width=160)
    st.title("RAG YouTuber Assistant")
    st.caption("Ask questions about my data engineering videos")

    
    text_input = st.text_input("Ask a question")

    if st.button("Send") and text_input.strip():
        try:
            response = requests.post(
                "http://127.0.0.1:8000/rag/query",
                json={"prompt": text_input},
                timeout=30,
            )
        except requests.exceptions.RequestException as e:
            st.error("❌ Could not connect to backend.")
            st.code(str(e))
            return

        
        if response.status_code != 200:
            st.error("❌ Backend error")
            st.code(response.text)
            return

        data = response.json()

        
        st.markdown("## Question")
        st.write(text_input)

        st.markdown("## Answer")
        st.write(data["answer"])

        st.markdown("## Source")
        st.code(data["filepath"])


if __name__ == "__main__":
    layout()
