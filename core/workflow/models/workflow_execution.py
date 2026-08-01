from dataclasses import dataclass, field
from datetime import datetime
import uuid

from core.application import ExecutionContext



@dataclass
class WorkflowExecution:


    input_event: object = None


    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )


    status: str = "CREATED"


    current_step: str = None


    state: dict = field(
        default_factory=dict
    )


    history: list = field(
        default_factory=list
    )


    finished_at: datetime = None


    context: ExecutionContext = None



    def __post_init__(self):

        if self.context is None:

            project_id = "workflow"


            if self.input_event:

                if hasattr(
                    self.input_event,
                    "project_id"
                ):

                    project_id = self.input_event.project_id



            self.context = ExecutionContext(

                project_id=project_id

            )