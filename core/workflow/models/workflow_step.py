from dataclasses import dataclass


@dataclass
class WorkflowStep:

    name: str

    handler: object = None

    output_key: str = None