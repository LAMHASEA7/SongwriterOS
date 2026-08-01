from core.agents.models import AgentCapability
from core.domain.models import Arrangement
from core.events.models import ArrangementCreatedEvent


class ArrangementAgent:

    name = "Arrangement Agent"

    capability = AgentCapability.ARRANGEMENT


    def __init__(self, event_bus):

        self.event_bus = event_bus


    def handle(self, event):

        arrangement = Arrangement(
            instruments="Electric guitar, bass, drums, piano",
            structure="Intro Verse Chorus Bridge Outro",
            atmosphere="Emotional cinematic rock"
        )


        print(
            f"{self.name} created: {arrangement}"
        )


        self.event_bus.publish(
            ArrangementCreatedEvent(
                arrangement=arrangement
            )
        )


        return arrangement