from langchain_core.embeddings import Embeddings
from langchain_openai import OpenAIEmbeddings

from app.core.config import settings


def get_embeddings() -> Embeddings:
    return OpenAIEmbeddings(
        model=settings.OPENAI_EMBEDDING_MODEL,
        api_key=settings.OPENAI_API_KEY,
    )


embedding = get_embeddings()
