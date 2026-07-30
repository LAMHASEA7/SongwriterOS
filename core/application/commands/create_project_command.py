from dataclasses import dataclass


@dataclass
class CreateProjectCommand:

    title: str

    project_type: str

    description: str = ""