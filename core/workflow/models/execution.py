from dataclasses import dataclass, field


@dataclass
class WorkflowExecution:

    input_event: object

    current_step: str = ""

    state: dict = field(
        default_factory=dict
    )