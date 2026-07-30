from dataclasses import dataclass
from .entity import Entity


@dataclass
class CreativeProject(Entity):

    title: str = ""
    project_type: str = ""
    status: str = "Draft"