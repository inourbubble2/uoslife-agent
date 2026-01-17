from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI

from app.core.config import settings


def get_chat_model() -> BaseChatModel:
    return ChatOpenAI(
        model=settings.OPENAI_CHAT_MODEL,
        api_key=settings.OPENAI_API_KEY,
    )


chat_model = get_chat_model()
