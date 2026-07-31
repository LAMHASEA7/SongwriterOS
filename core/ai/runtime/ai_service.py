from core.ai.runtime import ProviderRegistry


class AIService:

    def __init__(
        self,
        registry: ProviderRegistry,
        default_provider="mock provider"
    ):

        self.registry = registry
        self.default_provider = default_provider


    def generate(
        self,
        prompt
    ):

        provider = self.registry.get(
            self.default_provider
        )

        if provider is None:

            raise ValueError(
                f"Provider '{self.default_provider}' not found."
            )

        return provider.generate(
            prompt
        )