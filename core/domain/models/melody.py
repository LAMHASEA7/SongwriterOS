from dataclasses import dataclass
from .entity import Entity


@dataclass
class Melody(Entity):

    key: str = ""
    tempo: int = 0
    mood: str = ""
    description: str = ""