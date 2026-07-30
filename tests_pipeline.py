from core.events.bus.event_bus import EventBus

from core.events.models import (
    ProjectCreatedEvent,
    ConceptCreatedEvent
)

from core.agents.runtime import (
    ConceptAgent,
    LyricAgent
)

from core.infrastructure.repositories import (
    SQLiteWorkRepository
)


event_bus = EventBus()


work_repository = SQLiteWorkRepository(
    "database/songwriteros.db"
)


concept_agent = ConceptAgent(
    event_bus
)


lyric_agent = LyricAgent(
    work_repository
)


event_bus.subscribe(
    ProjectCreatedEvent,
    concept_agent.handle
)


event_bus.subscribe(
    ConceptCreatedEvent,
    lyric_agent.handle
)


event = ProjectCreatedEvent(
    "pipeline-test"
)


event_bus.publish(event)