📚 RAG YouTuber Assistant
En AI-driven RAG-applikation (Retrieval Augmented Generation) som svarar på frågor om data engineering-innehåll baserat på transkriptioner från YouTube-videor.
Projektet består av:

en Streamlit-frontend
en FastAPI-backend
en vektordatabas (LanceDB)
Gemini embeddings
Serverless deployment i Azure Functions


🚀 Översikt
Användaren kan ställa frågor som:
“Which SQL video should I watch?”
Systemet:
söker relevanta dokument i vektordatabasen
hämtar rätt kontext
genererar ett svar med hjälp av Gemini AI
Detta säkerställer att svaren baseras på faktiskt innehåll, inte hallucinationer.


🧠 Vad är RAG?
RAG (Retrieval Augmented Generation) innebär att:
AI-modellen inte gissar
den svarar endast utifrån lagrad data
I detta projekt:
YouTube-transkriptioner → embeddings
embeddings → lagras i LanceDB
frågor → matchas semantiskt
svar → genereras med Gemini


🏗️ Arkitektur
[ Streamlit Frontend ]
          |
          v
[ Azure Function (FastAPI) ]
          |
          v
[ LanceDB Vector Store ]
          |
          v
[ Gemini Embeddings & LLM ]
🧰 Tech Stack
Del	Teknik
Frontend	Streamlit
Backend	FastAPI
AI	Gemini (Google Generative AI)
Vector DB	LanceDB
Serverless	Azure Functions (Flex Consumption)
Deployment	Azure
Språk	Python 3.12

📁 Projektstruktur
.
├── api.py                   # FastAPI entry point for Azure Functions
├── function_app.py          # Azure Functions main configuration
├── ingestion.py             # Script to process and load transcripts into LanceDB
├── requirements.txt         # Project dependencies
├── backend/
│   ├── rag.py               # Core RAG logic (Gemini + Vector Search)
│   ├── data_models.py       # Pydantic models for API requests/responses
│   └── constants.py         # Configuration constants and prompts
├── frontend/
│   └── app.py               # Streamlit UI code
├── data/
│   └── transcripts/         # Raw markdown files containing YouTube transcripts
├── knowledge_base/          # Vector database storage (LanceDB)
│   └── articles.lance/      # Indexed data used for retrieval
├── assets/                  # Images and static files for the UI/README
└── explorations/            # Jupyter notebooks for testing and prototyping


⚙️ Köra projektet lokalt
1. Aktivera miljö
source venv/bin/activate
1. Indexera data
uv run ingestion.py
1. Starta backend
uvicorn api:app --reload
1. Starta frontend
uv run streamlit run frontend/app.py

☁️ Deployment i Azure
Backend är deployad som Azure Function App
API-nyckel sätts via Application Settings
Serverless → skalar automatiskt
🔗 Publikt API:
https://rag-youtube-rag.azurewebsites.net/rag/query
🔗 API-dokumentation:
https://rag-youtube-rag.azurewebsites.net/docs


🧪 Exempel på fråga
POST /rag/query
{
  "prompt": "Which SQL video do you recommend?"
}

✍️ Reflektion
Det mest utmanande var att:
integrera FastAPI med Azure Functions
hantera miljövariabler i molnet
Projektet gav djup förståelse för:
RAG-arkitektur
serverless deployment
AI-system i produktion


👤 Författare
Abdulrahman Fahmi
Data Engineering Student


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
