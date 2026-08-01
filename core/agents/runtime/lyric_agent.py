from core.agents.runtime.agent import Agent

from core.agents.models import AgentCapability

from core.domain.models import CreativeWork

from core.ai.prompts import LyricPrompt


class LyricAgent(Agent):

    name = "Lyric Agent"

    capability = AgentCapability.LYRICS


    def __init__(
        self,
        work_repository,
        ai_service
    ):

        self.work_repository = work_repository
        self.ai_service = ai_service


    def handle(
        self,
        event
    ):

        concept = event.state["concept"]

        prompt = LyricPrompt.from_concept(
            concept
        )

        response = self.ai_service.generate(
            prompt
        )

        work = CreativeWork(
            title=f"{concept.theme} Song",
            work_type="Lyrics",
            content=response.text
        )

        self.work_repository.save(
            work
        )

        print(
            "Lyric Agent saved:",
            work
        )

        return work