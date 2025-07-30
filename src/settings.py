from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    dummy_env_var: str = Field(default=...)


settings = Settings()  # from src.settings import settings
