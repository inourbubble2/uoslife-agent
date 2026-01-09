from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True, extra="ignore")

    PROJECT_NAME: str = "UOSLIFE Agent"
    DEBUG: bool = False

    DATABASE_URL: str = "postgresql+asyncpg://postgres:password@localhost:5432/uoslife_agent"

    OPENAI_API_KEY: str = ""

    LANGCHAIN_TRACING: bool = False
    LANGCHAIN_PROJECT: str = "uoslife-agent"


settings = Settings()
