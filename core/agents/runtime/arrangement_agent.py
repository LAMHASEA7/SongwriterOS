from core.agents.models import AgentCapability

from core.domain.models import Arrangement

from core.events.models import ArrangementCreatedEvent



class ArrangementAgent:


    name = "Arrangement Agent"


    capability = AgentCapability.ARRANGEMENT



    def __init__(
        self,
        event_bus,
        context=None
    ):

        self.event_bus = event_bus

        self.context = context



    def handle(
        self,
        event
    ):


        context = self.context



        if context:

            context.register_agent(
                self.name
            )


            context.register_event(
                "ArrangementAgentStarted"
            )



        #
        # Create Arrangement
        #

        arrangement = Arrangement(

            instruments="Electric guitar, bass, drums, piano",

            structure="Intro Verse Chorus Bridge Outro",

            atmosphere="Emotional cinematic rock"

        )



        print(
            f"{self.name} created: {arrangement}"
        )



        #
        # Attach Context
        #

        if context:


            context.register_arrangement(
                arrangement
            )


            context.register_event(
                "ArrangementCreatedEvent"
            )



            if context.song_project:


                context.song_project.attach_arrangement(
                    arrangement
                )



        #
        # Publish Event
        #

        if context and context.song_project:


            arrangement_event = ArrangementCreatedEvent(

                project_id=str(
                    context.song_project.id
                ),

                arrangement=arrangement

            )


            self.event_bus.publish(
                arrangement_event
            )


            print(
                "ArrangementCreatedEvent published"
            )



        return arrangement