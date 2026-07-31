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


# =========================
# Infrastructure
# =========================

event_bus = EventBus()


work_repository = SQLiteWorkRepository(
    "database/songwriteros.db"
)


# =========================
# AI Layer
# =========================

registry = ProviderRegistry()

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
# Workflow Definition
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
# Execute Workflow
# =========================

engine = WorkflowEngine()


event = ProjectCreatedEvent(
    "workflow-agent-test"
)


execution = engine.execute(
    workflow,
    event
)


# =========================
# Result
# =========================

print()

print("STATUS:")
print(execution.status)

print()

print("HISTORY:")
print(execution.history)