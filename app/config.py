# from pydantic import root_validator
# from pydantic.v1 import root_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    SECRET_KEY: str
    SECRET_ALGORITHM: str

    class Config:
        env_file = ".env"


settings = Settings()
# print(settings.DB_HOST)
# print(settings.DATABASE_URL)
print(settings.DATABASE_URL)

