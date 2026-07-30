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



engine = WorkflowEngine()


from core.events.models import ProjectCreatedEvent


event = ProjectCreatedEvent(
    "workflow-agent-test"
)


engine.execute(
    workflow,
    event
)