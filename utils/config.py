from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Config(BaseSettings):
    bot_token: SecretStr

    class Config:
        env_file = ".env"
