from core.agents.models import AgentCapability
from core.domain.models import Melody
from core.events.models import MelodyCreatedEvent


class MelodyAgent:

    name = "Melody Agent"
    capability = AgentCapability.MELODY


    def __init__(
        self,
        event_bus
    ):

        self.event_bus = event_bus


    def handle(
        self,
        event
    ) -> Melody:


        melody = Melody(
            key="G Major",
            tempo=92,
            mood="Emotional",
            description="Warm guitar driven melody"
        )


        print(
            f"{self.name} created: {melody}"
        )


        self.event_bus.publish(
            MelodyCreatedEvent(
                melody=melody
            )
        )


        return melody