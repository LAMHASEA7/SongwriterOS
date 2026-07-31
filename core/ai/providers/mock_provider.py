from core.ai.providers import AIProvider

from core.ai.models import AIResponse


class MockProvider(AIProvider):

    name = "Mock Provider"


    def generate(
        self,
        prompt
    ):

        return AIResponse(

            text=(
                "Mock response for: "
                + prompt.user
            ),

            model="mock-model",

            provider="mock"
        )