from core.agents.models import AgentCapability
from core.domain.models import Concept
from core.events.models import ConceptCreatedEvent


class ConceptAgent:

    name = "Concept Agent"
    capability = AgentCapability.CONCEPT


    def __init__(self, event_bus):

        self.event_bus = event_bus


    def handle(
        self,
        event: object
    ) -> Concept:

        concept = Concept(
            theme="Memory",
            emotion="Nostalgia",
            message="Keep the moment",
        )


        print(
            f"{self.name} created: {concept}"
        )


        self.event_bus.publish(
            ConceptCreatedEvent(
                concept=concept
            )
        )


        return concept