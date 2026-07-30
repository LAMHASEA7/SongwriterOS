from dataclasses import dataclass, field


@dataclass
class Workflow:

    name: str

    steps: list = field(
        default_factory=list
    )


    def add_step(self, step):

        self.steps.append(step)