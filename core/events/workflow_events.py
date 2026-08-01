from dataclasses import dataclass
from datetime import datetime



@dataclass
class WorkflowStartedEvent:
    """
    Published when workflow starts.
    """

    workflow_name: str

    project_id: str

    created_at: datetime




@dataclass
class WorkflowStepStartedEvent:
    """
    Published when a workflow step starts.
    """

    workflow_name: str

    step_name: str

    created_at: datetime




@dataclass
class WorkflowStepCompletedEvent:
    """
    Published when a workflow step completes.
    """

    workflow_name: str

    step_name: str

    status: str

    created_at: datetime




@dataclass
class WorkflowCompletedEvent:
    """
    Published when workflow finishes.
    """

    workflow_name: str

    project_id: str

    status: str

    created_at: datetime