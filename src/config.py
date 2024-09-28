from pydantic_settings import BaseSettings, SettingsConfigDict
import os

env_path = os.path.join(os.path.dirname(__file__), "..", "test.env" if "TEST" in os.environ else "test.env")

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorythm: str
    access_token_expire_minutes: str

    model_config = SettingsConfigDict(env_file=env_path, env_file_encoding="utf-8")

settings = Settings(_env_file=env_path, _env_file_encoding="utf-8")

