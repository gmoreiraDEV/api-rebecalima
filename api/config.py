
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "API - Rebeca Lima"
    admin_email: str
    items_per_user: int = 50
    database_url: str
    token_secret: str
    token_algorithm: str

    class Config:
        env_file = '.env'