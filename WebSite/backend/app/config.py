import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "VrukshaSetu API"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # Default: local SQLite for prototype/dev.
    # For Neon Postgres, set DATABASE_URL to:
    # postgresql+asyncpg://USER:PASSWORD@HOST/DATABASE?ssl=require
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "sqlite+aiosqlite:///./vrukshasetu.db"
    )

    JWT_SECRET: str = os.getenv("JWT_SECRET", "dev-secret-change-in-production-vrukshasetu")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

    CORS_ORIGINS: str = os.getenv(
        "CORS_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000"
    )

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]

    class Config:
        env_file = ".env"


settings = Settings()
