from dataclasses import dataclass

from .entity import Entity


@dataclass
class CreativeWork(Entity):

    title: str = ""

    work_type: str = ""

    content: str = ""