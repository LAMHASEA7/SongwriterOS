from dataclasses import dataclass

from .entity import Entity
from .work import CreativeWork
from .melody import Melody
from .arrangement import Arrangement


@dataclass
class Song(Entity):

    title: str = ""

    genre: str = ""

    status: str = "Draft"

    lyrics: CreativeWork | None = None

    melody: Melody | None = None

    arrangement: Arrangement | None = None



    def attach_lyrics(
        self,
        lyrics: CreativeWork
    ):

        self.lyrics = lyrics



    def attach_melody(
        self,
        melody: Melody
    ):

        self.melody = melody



    def attach_arrangement(
        self,
        arrangement: Arrangement
    ):

        self.arrangement = arrangement