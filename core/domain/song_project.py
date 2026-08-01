from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4



@dataclass
class SongProject:
    """
    Aggregate Root

    Represents a complete song creation project.
    Controls lifecycle of:
    - Concept
    - Lyrics
    - Melody
    - Arrangement
    """


    title: str


    id: UUID = field(
        default_factory=uuid4
    )


    created_at: datetime = field(
        default_factory=datetime.utcnow
    )


    #
    # Domain Objects
    #

    concept: object = None

    lyrics: object = None

    melody: object = None

    arrangement: object = None



    #
    # Lifecycle
    #

    status: str = "CREATED"



    #
    # Attach Concept
    #

    def attach_concept(
        self,
        concept
    ):

        self.concept = concept

        self.status = "CONCEPT_CREATED"



    #
    # Attach Lyrics
    #

    def attach_lyrics(
        self,
        lyrics
    ):

        self.lyrics = lyrics

        self.status = "LYRICS_CREATED"



    #
    # Attach Melody
    #

    def attach_melody(
        self,
        melody
    ):

        self.melody = melody

        self.status = "MELODY_CREATED"



    #
    # Attach Arrangement
    #

    def attach_arrangement(
        self,
        arrangement
    ):

        self.arrangement = arrangement

        self.status = "ARRANGEMENT_CREATED"



    #
    # Complete Project
    #

    def complete(
        self
    ):

        if (
            self.concept
            and self.lyrics
            and self.melody
            and self.arrangement
        ):

            self.status = "COMPLETED"



    #
    # Validation
    #

    def is_completed(
        self
    ):

        return self.status == "COMPLETED"



    #
    # Summary
    #

    def summary(
        self
    ):

        return {

            "id": str(self.id),

            "title": self.title,

            "status": self.status,

            "has_concept": self.concept is not None,

            "has_lyrics": self.lyrics is not None,

            "has_melody": self.melody is not None,

            "has_arrangement": self.arrangement is not None,

        }