# Cat Breed RAG Project 
 rag-youtuber-lab-Abdulrahman-fahmi

This project is a Retrieval-Augmented Generation (RAG) system that answers questions about cat breeds using Wikipedia data.
The answers are always based on retrieved documents and include the source file.

Cat Breeds Included

Abyssinian
Maine Coon
Bengal
Ragdoll
All information comes from Wikipedia articles.

Tech Stack

Python 3.12
FastAPI
Streamlit
LanceDB
pydantic-ai
Gemini embeddings

# activate environment
source .venv/bin/activate



# ingest data
uv run ingestion.py

# start backend
uvicorn api:app --reload

# start frontend
uv run streamlit run frontend/app.py

How It Works

PDFs from Wikipedia are converted to text
Text is embedded and stored in LanceDB
A question triggers vector search
The model answers using only retrieved content
The source file is shown
If the answer is not in the data, the system says so.

Author

Abdulrahman Fahmi
Data Engineering Student
