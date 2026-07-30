from dataclasses import dataclass
from .entity import Entity


@dataclass
class Agent(Entity):

    name: str = ""
    capability: str = ""