from dataclasses import dataclass
from core.domain.models import Melody


@dataclass
class MelodyCreatedEvent:

    melody: Melody