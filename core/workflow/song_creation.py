from core.workflow.models import Workflow
from core.workflow.models import WorkflowStep
from core.workflow.steps.agent_step import AgentStep

from core.events.models import (
    ConceptCreatedEvent,
    LyricsCreatedEvent,
    MelodyCreatedEvent
)


class SongCreationWorkflow:


    def __init__(
        self,
        concept_agent,
        lyric_agent,
        melody_agent,
        arrangement_agent,
        event_bus
    ):

        self.event_bus = event_bus

        self.workflow = Workflow(
            name="Song Creation"
        )

        self.workflow.event_bus = event_bus


        event_bus.subscribe(
            ConceptCreatedEvent,
            lyric_agent.handle
        )

        event_bus.subscribe(
            LyricsCreatedEvent,
            melody_agent.handle
        )

        event_bus.subscribe(
            MelodyCreatedEvent,
            arrangement_agent.handle
        )


        self.workflow.add_step(
            WorkflowStep(
                name="Generate Concept",
                handler=AgentStep(
                    name="Concept Agent",
                    agent=concept_agent,
                    event_factory=lambda execution:
                        execution.input_event,
                    output_key="concept"
                )
            )
        )


    def build(self):

        return self.workflow