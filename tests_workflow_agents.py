from core.workflow.engine import WorkflowEngine

from core.workflow.models import (
    Workflow,
    WorkflowStep
)

from core.agents.runtime import (
    ConceptAgent,
    LyricAgent
)

from core.events.bus.event_bus import EventBus

from core.infrastructure.repositories import (
    SQLiteWorkRepository
)

from core.ai.runtime import (
    ProviderRegistry,
    AIService
)

from core.ai.providers import (
    MockProvider
)

from core.events.models import (
    ProjectCreatedEvent
)

from core.config import settings


# =========================
# Infrastructure
# =========================

event_bus = EventBus()


work_repository = SQLiteWorkRepository(
    settings.database_path
)


# =========================
# AI Layer
# =========================

registry = ProviderRegistry()


if settings.ai_provider == "mock":

    registry.register(
        MockProvider()
    )


ai_service = AIService(
    registry
)


# =========================
# Agents
# =========================

concept_agent = ConceptAgent(
    event_bus
)


lyric_agent = LyricAgent(
    work_repository,
    ai_service
)


# =========================
# Workflow
# =========================

workflow = Workflow(
    "Song Creation Workflow"
)


workflow.add_step(
    WorkflowStep(
        "Create Concept",
        concept_agent.handle,
        "concept"
    )
)


workflow.add_step(
    WorkflowStep(
        "Create Lyrics",
        lyric_agent.handle
    )
)


# =========================
# Execute
# =========================

engine = WorkflowEngine()


event = ProjectCreatedEvent(
    "workflow-agent-test"
)


execution = engine.execute(
    workflow,
    event
)


print()

print("STATUS:")
print(execution.status)

print()

print("HISTORY:")
print(execution.history)