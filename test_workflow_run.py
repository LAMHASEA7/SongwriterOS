from core.events.bus.event_bus import EventBus

from core.agents.runtime.concept_agent import ConceptAgent
from core.agents.runtime.lyric_agent import LyricAgent

from core.workflow.engine import WorkflowEngine
from core.workflow.song_creation import SongCreationWorkflow

from core.events.models import ProjectCreatedEvent
from core.agents.runtime.melody_agent import MelodyAgent
from core.agents.runtime.arrangement_agent import ArrangementAgent

def main():

    print("START TEST")

    event_bus = EventBus()

    concept_agent = ConceptAgent(
        event_bus
    )
    lyric_agent = LyricAgent(
        event_bus
    )
    melody_agent = MelodyAgent(
        event_bus
    )
    arrangement_agent = ArrangementAgent(
    event_bus
    )
    workflow = SongCreationWorkflow(
        concept_agent,
        lyric_agent,
        melody_agent,
        arrangement_agent,
        event_bus
    ).build()

    engine = WorkflowEngine()

    event = ProjectCreatedEvent(
        project_id="demo-song-001"
    )

    execution = engine.execute(
        workflow,
        event
    )

    print(execution)


if __name__ == "__main__":
    main()