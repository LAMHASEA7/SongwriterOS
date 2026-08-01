from core.ai.providers import (
    MockProvider,
    OpenAIProvider
)


class ProviderFactory:

    @staticmethod
    def create(name: str):

        name = name.lower()

        if name == "mock":
            return MockProvider()

        if name == "openai":
            return OpenAIProvider()

        raise ValueError(
            f"Unknown provider: {name}"
        )