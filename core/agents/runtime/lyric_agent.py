from core.agents.models import AgentCapability
from core.domain.models import CreativeWork
from core.events.models import (
    ConceptCreatedEvent,
    LyricsCreatedEvent,
)


class LyricAgent:

    name = "Lyric Agent"
    capability = AgentCapability.LYRICS


    def __init__(self, event_bus):

        self.event_bus = event_bus


    def handle(
        self,
        event: ConceptCreatedEvent
    ) -> CreativeWork:


        work = CreativeWork(
    title="Memory",
    work_type="lyrics",
    content="Keep the moment alive"
        )


        print(
            f"{self.name} created: {work}"
        )


        self.event_bus.publish(
            LyricsCreatedEvent(
                work=work
            )
        )


        return work