from pydantic import BaseModel, Field

from app.infrastructure.agent_database.models.announcement import Announcement


class AgentResponse(BaseModel):
    answer: str = Field(description="The generated answer to the user's query")
    references: list[Announcement] = Field(default_factory=list, description="List of source announcements used")
    related_questions: list[str] = Field(default_factory=list, description="List of follow-up questions")
