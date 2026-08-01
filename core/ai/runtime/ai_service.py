import time

from core.ai.runtime import ProviderRegistry
from core.ai.models import AIResponse


class AIService:


    def __init__(
        self,
        registry: ProviderRegistry,
        default_provider="mock",
        context=None
    ):

        self.registry = registry

        self.default_provider = default_provider

        self.context = context



    def generate(
        self,
        prompt
    ):


        start_time = time.time()


        provider = self.registry.get(
            self.default_provider
        )


        if provider is None:

            raise ValueError(
                f"Provider '{self.default_provider}' not found."
            )


        print(
            "AI Request:",
            {
                "provider": self.default_provider,
                "system": prompt.system,
                "user": prompt.user
            }
        )


        try:


            response = provider.generate(
                prompt
            )


            elapsed = (
                time.time()
                -
                start_time
            )


            response.latency = round(
                elapsed,
                3
            )


            if self.context:

                self.context.register_ai_call()



            print(
                "AI Response:",
                {
                    "provider": response.provider,
                    "model": response.model,
                    "success": response.success,
                    "usage": response.usage,
                    "latency": response.latency
                }
            )


            return response



        except Exception as error:


            elapsed = (
                time.time()
                -
                start_time
            )


            if self.context:

                self.context.register_ai_call()



            print(
                "AI Error:",
                {
                    "provider": self.default_provider,
                    "error": str(error),
                    "latency": round(
                        elapsed,
                        3
                    )
                }
            )


            return AIResponse(

                success=False,

                error=str(error),

                provider=self.default_provider,

                latency=round(
                    elapsed,
                    3
                )

            )