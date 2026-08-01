from dataclasses import dataclass
from datetime import datetime



@dataclass
class LyricsCreatedEvent:


    project_id: str = ""

    lyrics: object = None

    created_at: datetime = None



    def __post_init__(self):

        if self.created_at is None:

            self.created_at = datetime.utcnow()