from dataclasses import dataclass
from .entity import Entity


@dataclass
class Concept(Entity):

    theme: str = ""
    emotion: str = ""
    message: str = ""