from dataclasses import dataclass
from datetime import datetime



@dataclass
class BaseEvent:
    """
    Base domain event.
    """

    created_at: datetime = None


    def __post_init__(self):

        if self.created_at is None:

            self.created_at = datetime.utcnow()



@dataclass
class ProjectCreatedEvent(BaseEvent):

    project_id: str = ""



@dataclass
class ConceptCreatedEvent(BaseEvent):

    project_id: str = ""

    concept: object = None



@dataclass
class LyricsCreatedEvent(BaseEvent):

    project_id: str = ""

    lyrics: object = None



@dataclass
class MelodyCreatedEvent(BaseEvent):

    project_id: str = ""

    melody: object = None



@dataclass
class ArrangementCreatedEvent(BaseEvent):

    project_id: str = ""

    arrangement: object = None