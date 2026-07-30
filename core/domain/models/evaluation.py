from dataclasses import dataclass
from .entity import Entity


@dataclass
class Evaluation(Entity):

    score: float = 0
    comment: str = ""