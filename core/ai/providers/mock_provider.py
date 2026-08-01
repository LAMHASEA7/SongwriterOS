from core.ai.providers import AIProvider

from core.ai.models import AIResponse


class MockProvider(AIProvider):

    name = "mock"


    def generate(
        self,
        prompt
    ):

        user_prompt = prompt.user.lower()


        # Concept generation
        if "concept" in user_prompt or "theme" in user_prompt:

            return AIResponse(

                text=(
                    "{"
                    "\"theme\":\"Lost Memories\","
                    "\"emotion\":\"Nostalgia\","
                    "\"message\":\"A song about memories that never disappear\""
                    "}"
                ),

                model="mock-model",

                provider="mock"

            )


        # Lyrics generation
        if "lyrics" in user_prompt or "song" in user_prompt:

            return AIResponse(

                text=(
                    "Verse 1:\n"
                    "I remember the days we shared\n"
                    "Moments floating in the air\n\n"

                    "Chorus:\n"
                    "Keep the memories alive\n"
                    "Even when the years go by"
                ),

                model="mock-model",

                provider="mock"

            )


        # Default response

        return AIResponse(

            text=(
                "Mock response for: "
                + prompt.user
            ),

            model="mock-model",

            provider="mock"

        )