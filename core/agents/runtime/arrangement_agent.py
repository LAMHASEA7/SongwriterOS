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



        arrangement = Arrangement(

            instruments="Electric guitar, bass, drums, piano",

            structure="Intro Verse Chorus Bridge Outro",

            atmosphere="Emotional cinematic rock"

        )



        print(
            f"{self.name} created: {arrangement}"
        )



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



        self.event_bus.publish(

            ArrangementCreatedEvent(

                arrangement=arrangement

            )

        )



        return arrangement