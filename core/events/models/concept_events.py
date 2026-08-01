from dataclasses import dataclass
from datetime import datetime


@dataclass
class ConceptCreatedEvent:


    project_id: str = ""

    concept: object = None

    created_at: datetime = None



    def __post_init__(self):

        if self.created_at is None:

            self.created_at = datetime.utcnow()