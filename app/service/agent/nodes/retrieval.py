from typing import Any

from app.infrastructure.vector_store.vector_store import get_vector_store
from app.service.agent.schema.reference import Reference
from app.service.agent.schema.state import GraphState


async def retrieval_node(state: GraphState) -> dict[str, Any]:
    query = state.get("rewritten_query") or state["user_query"]

    vector_store = await get_vector_store()

    docs_with_scores = await vector_store.asimilarity_search_with_relevance_scores(query, k=5)

    references = [
        Reference(
            announcement_id=doc.metadata.get("announcement_id"),
            chunk_index=doc.metadata.get("chunk_index"),
            title=doc.metadata.get("title"),
            content=doc.page_content,
            url=doc.metadata.get("url"),
            score=score,
        )
        for (doc, score) in docs_with_scores
    ]

    return {"references": references}
