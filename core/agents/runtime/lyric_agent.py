from core.agents.runtime.agent import Agent

from core.agents.models import AgentCapability

from core.domain.models import CreativeWork

from core.ai.prompts import LyricPrompt



class LyricAgent(Agent):

    name = "Lyric Agent"

    capability = AgentCapability.LYRICS



    def __init__(
        self,
        work_repository,
        ai_service,
        context=None
    ):

        self.work_repository = work_repository

        self.ai_service = ai_service

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
                "LyricAgentStarted"
            )



        concept = event.concept



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
            "AI Response:",
            response
        )


        print(
            "AI Text:",
            response.text
        )



        work = CreativeWork(

            title=f"{concept.theme} Song",

            work_type="Lyrics",

            content=response.text

        )



        self.work_repository.save(
            work
        )



        print(
            "Lyric Agent saved:",
            work
        )



        if context:


            context.register_work(
                work
            )


            context.register_event(
                "LyricsCreatedEvent"
            )


            if context.song_project:


                context.song_project.attach_lyrics(
                    work
                )



        return work