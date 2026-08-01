from openai import OpenAI, OpenAIError

from core.config import settings

from .provider import AIProvider

from core.ai.models import AIResponse


class OpenAIProvider(AIProvider):

    name = "openai"


    def __init__(self):

        self.client = OpenAI(
            api_key=settings.openai_api_key
        )


    def generate(
        self,
        prompt
    ):

        try:

            response = self.client.responses.create(
                model=settings.ai_model,
                max_output_tokens=settings.ai_max_output_tokens,
                input=[
                    {
                        "role": "system",
                        "content": prompt.system
                    },
                    {
                        "role": "user",
                        "content": prompt.user
                    }
                ]
            )


            usage = {}

            if response.usage:

                usage = {
                    "input_tokens": response.usage.input_tokens,
                    "output_tokens": response.usage.output_tokens
                }


            return AIResponse(
                text=response.output_text,
                model=settings.ai_model,
                provider=self.name,
                usage=usage,
                success=True
            )


        except OpenAIError as e:

            return AIResponse(
                text="",
                model=settings.ai_model,
                provider=self.name,
                success=False,
                error=str(e)
            )