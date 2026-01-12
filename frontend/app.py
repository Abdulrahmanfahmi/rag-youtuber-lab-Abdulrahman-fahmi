import streamlit as st
import requests
from pathlib import Path

st.set_page_config(
    page_title="RAG YouTuber Assistant",
    page_icon="📚",
    layout="wide",
)

ASSETS_PATH = Path(__file__).parents[1] / "assets"
BACKEND_URL = "https://rag-youtube-rag.azurewebsites.net/rag/query"



if "messages" not in st.session_state:
    st.session_state.messages = []


def main():
    col1, col2 = st.columns([1, 4])

    with col1:
        st.image(ASSETS_PATH / "abdulrahman.png", width=140)

    with col2:
        st.title("RAG YouTuber Assistant")
        st.caption("Ask questions about my data engineering videos")

    st.divider()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Ask a question about the videos...")

    if user_input:
        
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        
        try:
            response = requests.post(
                BACKEND_URL,
                json={"prompt": user_input},
                timeout=30,
            )
            response.raise_for_status()
            data = response.json()

            answer = data["answer"]
           
            bot_message = answer

           # source = data["filepath"]

           # bot_message = f"{answer}\n\n**Source:** `{source}`"

        except Exception as e:
            bot_message = f" Backend error:\n```\n{e}\n```"

        
        st.session_state.messages.append(
            {"role": "assistant", "content": bot_message}
        )

        with st.chat_message("assistant"):
            st.markdown(bot_message)


if __name__ == "__main__":
    main()
