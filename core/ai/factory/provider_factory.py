from core.ai.providers import MockProvider


class ProviderFactory:

    @staticmethod
    def create(name: str):

        name = name.lower()

        if name == "mock":

            return MockProvider()

        raise ValueError(
            f"Unknown provider: {name}"
        )