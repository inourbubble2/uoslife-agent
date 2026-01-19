from langchain_core.vectorstores import VectorStore
from langchain_postgres import PGEngine, PGVectorStore

from app.infrastructure.agent_database.database import engine
from app.infrastructure.ai import get_embeddings


async def get_vector_store() -> VectorStore:
    pg_engine = PGEngine.from_engine(engine=engine)
    embedding = get_embeddings()

    return await PGVectorStore.create(
        engine=pg_engine,
        table_name="announcement_embedding",
        embedding_service=embedding,
        id_column="id",
        content_column="document",
        embedding_column="embedding",
        metadata_columns=[
            "chunk_index",
            "announcement_id",
            "author",
            "board",
            "title",
            "major",
            "url",
            "written_at",
        ],
    )
