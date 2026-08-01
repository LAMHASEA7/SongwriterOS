from dataclasses import dataclass
from .entity import Entity


@dataclass
class Arrangement(Entity):

    instruments: str = ""
    structure: str = ""
    atmosphere: str = ""