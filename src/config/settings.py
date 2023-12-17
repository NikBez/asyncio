from dataclasses import dataclass

from environs import Env
import os

env = Env()
env.read_env()


db_name = env.str("POSTGRES_DB")
db_user = env.str("POSTGRES_USER")
db_password = env.str("POSTGRES_PASSWORD")
db_host = env.str("POSTGRES_HOST", "localhost")
db_port = env.str("POSTGRES_PORT", "5432")
chunk_size = env.int("CHUNK_SIZE", 10)


@dataclass
class Settings:
    db_url: str = (
        f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    chunk_size: int = chunk_size


settings = Settings()
