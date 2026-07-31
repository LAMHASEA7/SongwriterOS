from dataclasses import dataclass


@dataclass
class Settings:

    ai_provider: str = "mock provider"

    database_path: str = (
        "database/songwriteros.db"
    )


settings = Settings()