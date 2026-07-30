from dataclasses import dataclass
from .entity import Entity


@dataclass
class Knowledge(Entity):

    topic: str = ""
    description: str = ""