from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage

from app.infrastructure.ai import get_chat_model
from app.service.agent.schema.state import GraphState

SYSTEM_PROMPT = """You are a query rewriter for a vector database search system used by university students.
Your goal is to optimize the user's query to maximize retrieval accuracy for school announcements.

Instructions:
1. Remove conversational filler (e.g., "hello", "I want to know about", "can you tell me").
2. Extract key entities (e.g., specific departments, scholarship names, event types) and intent.
3. Keep the query concise and keyword-focused.
4. If the query is already simple and clear, return it as is.
5. Do NOT output any explanation, just the rewritten query string.
"""


async def rewriting_node(state: GraphState) -> dict[str, Any]:
    chat_model = get_chat_model()
    user_query = state["user_query"]

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_query),
    ]

    response = await chat_model.ainvoke(messages)
    rewritten_query = str(response.content)

    return {"rewritten_query": rewritten_query}
