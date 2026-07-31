from core.domain.models import Concept
from core.events.models import ConceptCreatedEvent
from core.agents.models import AgentCapability


class ConceptAgent:

    name = "Concept Agent"
    capability = AgentCapability.CONCEPT

    def __init__(self, event_bus):

        self.event_bus = event_bus

    def handle(self, event):

        concept = Concept(
            theme="Memory",
            emotion="Nostalgia",
            message="Keep the moment"
        )

        print(
            f"Concept Agent created: {concept}"
        )

        return concept