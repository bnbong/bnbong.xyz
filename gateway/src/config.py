# --------------------------------------------------------------------------
# Configuration settings for Bifrost API Gateway
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
import os
from typing import List


class Settings:
    """Application settings"""

    # Environment
    ENVIRONMENT: str = "development"
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"

    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Security
    ALLOWED_HOSTS: List[str] = ["*"]
    ALLOWED_ORIGINS: List[str] = ["*"]

    # Auth Server
    AUTH_SERVER_URL: str = "http://auth-server:8001"

    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 60

    # Redis
    REDIS_URL: str = "redis://redis:6379/0"

    # Database
    DATABASE_URL: str = "postgresql://bnbong:password@postgres:5432/bnbong"

    # Service Registry
    SERVICES_CONFIG_PATH: str = "/app/config/services.json"

    # Monitoring
    ENABLE_METRICS: bool = True

    def __init__(self) -> None:
        # Load from environment variables
        self.ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
        self.DEBUG = os.getenv("DEBUG", "false").lower() == "true"
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
        self.HOST = os.getenv("HOST", "0.0.0.0")
        self.PORT = int(os.getenv("PORT", "8000"))
        self.AUTH_SERVER_URL = os.getenv("AUTH_SERVER_URL", "http://auth-server:8001")
        self.RATE_LIMIT_PER_MINUTE = int(os.getenv("RATE_LIMIT_PER_MINUTE", "60"))
        self.REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
        self.DATABASE_URL = os.getenv(
            "DATABASE_URL", "postgresql://bnbong:password@postgres:5432/bnbong"
        )
        self.SERVICES_CONFIG_PATH = os.getenv(
            "SERVICES_CONFIG_PATH", "/app/config/services.json"
        )
        self.ENABLE_METRICS = os.getenv("ENABLE_METRICS", "true").lower() == "true"

        # Parse lists
        self.ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")
        self.ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")


settings = Settings()
