from pydantic import BaseModel, Field
from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector
from dotenv import load_dotenv

load_dotenv()


embedding_model = (
    get_registry()
    .get("gemini-text")
    .create(name="gemini-embedding-001")
)

EMBEDDING_DIM = 3072


class Article(LanceModel):
    doc_id: str
    filepath: str
    filename: str
    content: str = embedding_model.SourceField()
    embedding: Vector(EMBEDDING_DIM) = embedding_model.VectorField()


class Prompt(BaseModel):
    prompt: str


class RagResponse(BaseModel):
    filename: str
    filepath: str
    answer: str







