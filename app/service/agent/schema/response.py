from pydantic import BaseModel, Field

from app.service.agent.schema.reference import Reference


class AgentResponse(BaseModel):
    answer: str = Field(description="The generated answer to the user's query")
    references: list[Reference] = Field(default_factory=list, description="List of source announcements used")
    related_questions: list[str] = Field(default_factory=list, description="List of follow-up questions")
