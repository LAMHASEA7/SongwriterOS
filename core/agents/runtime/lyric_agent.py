from core.agents.runtime.agent import Agent
from core.domain.models import CreativeWork
from core.agents.models import AgentCapability


class LyricAgent(Agent):

    name = "Lyric Agent"
    capability = AgentCapability.LYRICS

    def __init__(
        self,
        work_repository
    ):

        self.work_repository = work_repository

    def handle(
        self,
        event
    ):

        concept = event.state["concept"]

        work = CreativeWork(

            title=f"{concept.theme} Song",

            work_type="Lyrics",

            content=(
                "A song about "
                + concept.theme
            )

        )

        self.work_repository.save(
            work
        )

        print(
            "Lyric Agent saved:",
            work
        )

        return work