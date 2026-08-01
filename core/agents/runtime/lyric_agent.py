from core.agents.runtime.agent import Agent

from core.agents.models import AgentCapability

from core.domain.models import CreativeWork

from core.ai.prompts import LyricPrompt

from core.events.models import LyricsCreatedEvent


class LyricAgent(Agent):

    name = "Lyric Agent"

    capability = AgentCapability.LYRICS


    def __init__(
        self,
        event_bus,
        ai_service,
        context=None
    ):

        self.event_bus = event_bus

        self.ai_service = ai_service

        self.context = context



    def handle(
        self,
        event
    ):


        context = self.context



        #
        # Register Agent
        #

        if context:

            context.register_agent(
                self.name
            )



        #
        # Receive Concept Event
        #

        concept = event.concept



        #
        # Generate Lyrics
        #

        prompt = LyricPrompt.from_concept(
            concept
        )


        response = self.ai_service.generate(
            prompt
        )



        if not response.success:

            print(
                "Lyric generation failed:",
                response.error
            )

            return None



        print(
            "AI Text:",
            response.text
        )



        #
        # Create Domain Object
        #

        work = CreativeWork(

            title=f"{concept.theme} Song",

            work_type="Lyrics",

            content=response.text

        )



        #
        # Attach to Context
        #

        if context:


            context.register_work(
                work
            )


            if context.song_project:

                context.song_project.attach_lyrics(
                    work
                )



        #
        # Publish Event
        #

        if context and context.song_project:


            lyrics_event = LyricsCreatedEvent(

                project_id=str(
                    context.song_project.id
                ),

                lyrics=work

            )


            self.event_bus.publish(
                lyrics_event
            )


            print(
                "LyricsCreatedEvent published"
            )



        else:

            print(
                "LyricsCreatedEvent skipped: no project context"
            )



        return work