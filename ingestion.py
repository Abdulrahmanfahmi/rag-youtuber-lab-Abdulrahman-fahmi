import time
from pathlib import Path
import lancedb

from backend.constants import VECTOR_DATABASE_PATH, DATA_PATH
from backend.data_models import Article


def setup_vector_db(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)
    db = lancedb.connect(path)
    db.create_table("articles", schema=Article, exist_ok=True)
    return db


def ingest_docs(table):
    files = list(DATA_PATH.glob("*.md"))
    print(f"Found {len(files)} markdown files")

    for i, file in enumerate(files, start=1):
        print(f"[{i}/{len(files)}] Ingesting {file.name}")

        content = file.read_text(encoding="utf-8")
        doc_id = file.stem

        
        table.delete(f"doc_id = '{doc_id}'")

        table.add([
            {
                "doc_id": doc_id,
                "filepath": str(file),
                "filename": file.name,
                "content": content,
            }
        ])

        time.sleep(12)

    print("✅ Ingestion completed")


if __name__ == "__main__":
    db = setup_vector_db(VECTOR_DATABASE_PATH)
    ingest_docs(db["articles"])
