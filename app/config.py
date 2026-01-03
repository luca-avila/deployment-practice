from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """ """
    APP_NAME: str = 'Deployment practice'
    DEBUG: bool = True
    DB_ECHO: bool = True

    # Required from .env
    DATABASE_URL: str 
    SECRET_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )

settings = Settings()

