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


        self.workflow = Workflow(
            name="Song Creation"
        )


        self.workflow.set_event_bus(
            event_bus
        )


        #
        # Share ExecutionContext
        #

        self.context = concept_agent.context

        self.workflow.context = self.context



        #
        # Step 1 Concept
        #

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



        #
        # Step 2 Lyrics
        #

        self.workflow.add_step(

            WorkflowStep(

                name="Generate Lyrics",

                handler=AgentStep(

                    name="Lyric Agent",

                    agent=lyric_agent,

                    event_factory=lambda execution:

                        ConceptCreatedEvent(

                            project_id=str(
                                execution.context.song_project.id
                            ),

                            concept=execution.state[
                                "concept"
                            ]

                        ),

                    output_key="lyrics"

                )

            )

        )



        #
        # Step 3 Melody
        #

        self.workflow.add_step(

            WorkflowStep(

                name="Generate Melody",

                handler=AgentStep(

                    name="Melody Agent",

                    agent=melody_agent,

                    event_factory=lambda execution:

                        LyricsCreatedEvent(

                            project_id=str(
                                execution.context.song_project.id
                            ),

                            lyrics=execution.state[
                                "lyrics"
                            ]

                        ),

                    output_key="melody"

                )

            )

        )



        #
        # Step 4 Arrangement
        #

        self.workflow.add_step(

            WorkflowStep(

                name="Generate Arrangement",

                handler=AgentStep(

                    name="Arrangement Agent",

                    agent=arrangement_agent,

                    event_factory=lambda execution:

                        MelodyCreatedEvent(

                            project_id=str(
                                execution.context.song_project.id
                            ),

                            melody=execution.state[
                                "melody"
                            ]

                        ),

                    output_key="arrangement"

                )

            )

        )



    def build(self):

        return self.workflow