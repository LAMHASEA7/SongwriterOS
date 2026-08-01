from dataclasses import dataclass, field



@dataclass
class Workflow:


    name: str


    steps: list = field(
        default_factory=list
    )


    event_bus: object = None



    def add_step(
        self,
        step
    ):

        self.steps.append(
            step
        )



    def set_event_bus(
        self,
        event_bus
    ):

        self.event_bus = event_bus