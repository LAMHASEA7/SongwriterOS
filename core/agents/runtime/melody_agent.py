from core.agents.models import AgentCapability

from core.domain.models import Melody

from core.events.models import MelodyCreatedEvent



class MelodyAgent:


    name = "Melody Agent"


    capability = AgentCapability.MELODY



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
    ) -> Melody:


        context = self.context



        if context:

            context.register_agent(
                self.name
            )


            context.register_event(
                "MelodyAgentStarted"
            )



        melody = Melody(

            key="G Major",

            tempo=92,

            mood="Emotional",

            description="Warm guitar driven melody"

        )



        print(
            f"{self.name} created: {melody}"
        )



        if context:


            context.register_melody(
                melody
            )


            context.register_event(
                "MelodyCreatedEvent"
            )


            if context.song_project:

                context.song_project.attach_melody(
                    melody
                )



        self.event_bus.publish(

            MelodyCreatedEvent(

                melody=melody

            )

        )



        return melody