from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./asset_tracker.db"
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "Asset Tracker"

    class Config:
        env_file = ".env"

settings = Settings()
