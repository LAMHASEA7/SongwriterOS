from dataclasses import dataclass
from core.domain.models import Arrangement


@dataclass
class ArrangementCreatedEvent:

    arrangement: Arrangement