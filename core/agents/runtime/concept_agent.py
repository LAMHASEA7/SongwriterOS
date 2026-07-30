from core.domain.models import Concept
from core.events.models import ConceptCreatedEvent


class ConceptAgent:

    name = "Concept Agent"


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