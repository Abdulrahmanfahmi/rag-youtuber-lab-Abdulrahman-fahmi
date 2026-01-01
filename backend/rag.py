from pydantic_ai import Agent
from backend.data_models import RagResponse
from backend.constants import VECTOR_DATABASE_PATH
import lancedb


vector_db = lancedb.connect(uri=VECTOR_DATABASE_PATH)


rag_agent = Agent(
    model="google-gla:gemini-2.5-flash",
    retries=2,
    system_prompt=(
    "You are a data engineering youtuber who explains concepts clearly and pedagogically.",
    "Answer questions based only on the retrieved video transcripts.",
    "Use simple but correct technical language.",
    "If the answer is not found in the transcripts, say that you cannot answer.",
    "Keep the answer concise, maximum 6 sentences.",
    "Always mention which transcript file was used as source.",
),
    output_type=RagResponse,
)


@rag_agent.tool_plain
def retrieve_top_documents(query: str, k=3) -> str:
    results = vector_db["articles"].search(query=query).limit(k).to_list()

    if not results:
        return "NO_RELEVANT_DOCUMENTS_FOUND"

    doc = results[0]

    return f"""
    
    Filename: {doc["filename"]}
    Filepath: {doc["filepath"]}
    Content: {doc["content"]}
"""