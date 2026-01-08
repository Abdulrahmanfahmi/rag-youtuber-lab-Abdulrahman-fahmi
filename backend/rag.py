from pydantic_ai import Agent
from backend.data_models import RagResponse
from backend.constants import VECTOR_DATABASE_PATH
import lancedb


vector_db = lancedb.connect(uri=VECTOR_DATABASE_PATH)


rag_agent = Agent(
    model="google-gla:gemini-2.5-flash",
    retries=2,
    system_prompt=(
        "You are a Data Engineering Youtuber teaching in your videos."
        "You like Pokemon, you are always happy when you succeed in your coding, and you have a nerdy humour."
        "Your answer ALWAYS has to be based on the retrieved knowledge. If you think it's not enough, you can add 1-2 sentences of your own knowledge, because you don't like to leave your audience without any answer."
        "Your answer has to be rather short and clear to fulfill the user's prompt."
        "ALWAYS explicitly mention the video title and the filename you used to answer the question."
        "If you cannot find the answer in the context and the user prompt is outside the retrieved knowledge, say 'I don't know'.",
    ),
    output_type=RagResponse,
)


@rag_agent.tool_plain
def retrieve_top_documents(query: str, k: int = 3) -> str:
    results = vector_db["articles"].search(query).limit(k).to_list()

    if not results:
        return "NO_RELEVANT_DOCUMENTS_FOUND"

    context = []
    for r in results:
        context.append(
            f"""
Filename: {r['filename']}
Filepath: {r['filepath']}
Content:
{r['content']}
"""
        )

    return "\n\n".join(context)
