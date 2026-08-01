import os

from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:

    ai_provider: str = (
        os.getenv(
            "AI_PROVIDER",
            "mock"
        )
    )

    ai_model: str = (
        os.getenv(
            "AI_MODEL",
            "gpt-5.5"
        )
    )
    ai_max_output_tokens: int = int(
    os.getenv(
        "AI_MAX_OUTPUT_TOKENS",
        "1000"
        )
    )
    database_path: str = (
        os.getenv(
            "DATABASE_PATH",
            "database/songwriteros.db"
        )
    )

    openai_api_key: str = os.getenv(
        "OPENAI_API_KEY",
        ""
    )


settings = Settings()