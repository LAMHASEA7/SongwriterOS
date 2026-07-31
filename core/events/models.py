from dataclasses import dataclass
from core.domain.models import Concept


@dataclass
class ConceptCreatedEvent:

    concept: Concept