from dataclasses import dataclass
from datetime import datetime



@dataclass
class WorkflowStartedEvent:

    workflow_name: str

    project_id: str

    created_at: datetime



@dataclass
class WorkflowStepStartedEvent:

    workflow_name: str

    step_name: str

    created_at: datetime



@dataclass
class WorkflowStepCompletedEvent:

    workflow_name: str

    step_name: str

    status: str

    created_at: datetime



@dataclass
class WorkflowCompletedEvent:

    workflow_name: str

    project_id: str

    status: str

    created_at: datetime