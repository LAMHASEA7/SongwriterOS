from core.events.bus.event_bus import EventBus
from core.events.models import ProjectCreatedEvent

from core.agents.registry import AgentRegistry

from core.agents.runtime import (
    ConceptAgent,
    LyricAgent,
    AgentDispatcher
)


event_bus = EventBus()


registry = AgentRegistry()


registry.register(
    ConceptAgent()
)


registry.register(
    LyricAgent()
)


dispatcher = AgentDispatcher(
    registry
)


event_bus.subscribe(
    ProjectCreatedEvent,
    dispatcher.handle
)


event = ProjectCreatedEvent(
    "registry-agent-test"
)


event_bus.publish(event)