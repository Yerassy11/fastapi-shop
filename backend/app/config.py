from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings."""

    app_name: str = "FastAPI Shop"
    debug: bool = True
    database_url: str = "sqlite:///./test.db"
    cors_origins: list[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]
    static_dir: str = "static"
    images_dir: str = "images"
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()