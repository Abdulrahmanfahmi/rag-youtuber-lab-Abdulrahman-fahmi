from backend.constants import VECTOR_DATABASE_PATH, DATA_PATH
from backend.data_models import Article
import lancedb
from pathlib import Path



def setup_vector_db(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)
    vector_db = lancedb.connect(uri=path)
    vector_db.create_table("articles", schema=Article, exist_ok=True)
    return vector_db


def ingest_docs_to_vector_db(table):
    for file in DATA_PATH.glob("transcripts/*.md"):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        doc_id = file.stem

        # Remove existing document if it exists
        table.delete(f"doc_id = '{doc_id}'")

        table.add(
            [
                {
                    "doc_id": doc_id,
                    "filepath": str(file),
                    "filename": file.name,
                    "content": content,
                }
            ]
        )

        df = table.to_pandas()
        print(f"Ingested: {file.name}")
        print(f"Current table shape: {df.shape}")

        


if __name__ == "__main__":
    vector_db = setup_vector_db(VECTOR_DATABASE_PATH)
    ingest_docs_to_vector_db(vector_db["articles"])
