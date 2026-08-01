from dataclasses import dataclass

from core.domain.models import CreativeWork


@dataclass
class LyricsCreatedEvent:

    work: CreativeWork