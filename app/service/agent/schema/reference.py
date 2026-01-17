from pydantic import BaseModel, Field


class Reference(BaseModel):
    announcement_id: int = Field(description="The unique ID of the announcement")
    chunk_index: int = Field(description="The index of the text chunk within the announcement")
    title: str = Field(description="The title of the announcement")
    content: str = Field(description="The text content of the announcement")
    url: str = Field(description="The URL link to the original announcement")
    score: float = Field(description="The relevance score of the announcement")
