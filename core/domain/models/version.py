from dataclasses import dataclass
from .entity import Entity


@dataclass
class Version(Entity):

    version_number: str = "1.0"
    description: str = ""