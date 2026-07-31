from core.ai.models import Prompt


class LyricPrompt:

    @staticmethod
    def from_concept(
        concept
    ):

        return Prompt(

            system=(
                "You are a professional songwriter."
            ),

            user=(
                f"Write song lyrics about '{concept.theme}'. "
                f"Emotion: {concept.emotion}. "
                f"Message: {concept.message}."
            )

        )