from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    db_user: str
    db_password: str
    db_name: str
    pgadmin_email: str
    pgadmin_password: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


    class Config:
        env_file = ".env"

settings = Settings()