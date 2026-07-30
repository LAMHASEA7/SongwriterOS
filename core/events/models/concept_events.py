from core.events.event import Event


class ConceptCreatedEvent(Event):

    def __init__(
        self,
        concept
    ):

        super().__init__()

        self.concept = concept