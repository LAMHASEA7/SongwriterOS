from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class WorkflowExecution:

    input_event: object = None

    current_step: str = ""

    state: dict = field(default_factory=dict)

    history: list = field(default_factory=list)

    status: str = "PENDING"

    started_at: datetime = field(
        default_factory=datetime.utcnow
    )

    finished_at: datetime = None