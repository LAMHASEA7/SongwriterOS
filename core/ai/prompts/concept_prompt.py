from core.ai.models import Prompt


class ConceptPrompt:


    @staticmethod
    def create():

        return Prompt(

            system=(
                "You are a professional songwriter "
                "and creative director."
            ),

            user=(
                "Create a song concept.\n\n"
                "Return ONLY valid JSON.\n"
                "Format:\n"
                "{\n"
                '  "theme": "",\n'
                '  "emotion": "",\n'
                '  "message": ""\n'
                "}"

            )

        )