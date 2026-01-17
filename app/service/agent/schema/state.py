from typing import TypedDict

from app.service.agent.schema.intention import Intention
from app.service.agent.schema.reference import Reference
from app.service.agent.schema.response import AgentResponse


class GraphState(TypedDict):
    user_query: str
    intention: Intention | None
    rewritten_query: str | None
    references: list[Reference] | None
    response: AgentResponse | None
    is_verified: bool | None  # TODO: Change to enum (GOOD, INSUFFICIENT_CONTEXT, PRIVACY_VIOLATED, ...)
