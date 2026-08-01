from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class SongProject:

    title: str

    id: UUID = field(
        default_factory=uuid4
    )

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )


    concept: object = None

    lyrics: object = None

    melody: object = None

    arrangement: object = None


    status: str = "CREATED"



    def attach_concept(
        self,
        concept
    ):

        self.concept = concept
        self.status = "CONCEPT_CREATED"



    def attach_lyrics(
        self,
        lyrics
    ):

        self.lyrics = lyrics
        self.status = "LYRICS_CREATED"



    def attach_melody(
        self,
        melody
    ):

        self.melody = melody
        self.status = "MELODY_CREATED"



    def attach_arrangement(
        self,
        arrangement
    ):

        self.arrangement = arrangement
        self.status = "COMPLETED"