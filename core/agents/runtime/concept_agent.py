import json

from core.agents.models import AgentCapability

from core.domain.models import Concept

from core.events.models import ConceptCreatedEvent

from core.ai.prompts import ConceptPrompt



class ConceptAgent:

    name = "Concept Agent"

    capability = AgentCapability.CONCEPT



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
        event: object
    ) -> Concept:


        context = self.context


        if context:

            context.register_agent(
                self.name
            )


            context.register_event(
                "ConceptAgentStarted"
            )



        prompt = ConceptPrompt.create()



        response = self.ai_service.generate(
            prompt
        )



        if not response.success:

            print(
                "Concept generation failed:",
                response.error
            )


            concept = self._fallback_concept()



        else:

            print(
                "AI Response:",
                response.text
            )


            concept = self._parse_concept(
                response.text
            )



        print(
            f"{self.name} created:",
            concept
        )



        if context:

            context.register_concept(
                concept
            )


            if context.song_project:

                context.song_project.attach_concept(
                    concept
                )


            context.register_event(
                "ConceptCreatedEvent"
            )



        self.event_bus.publish(

            ConceptCreatedEvent(
                concept=concept
            )

        )



        return concept





    def _parse_concept(
        self,
        text: str
    ) -> Concept:


        try:

            data = json.loads(
                text
            )


            return Concept(

                theme=data.get(
                    "theme",
                    "Unknown"
                ),

                emotion=data.get(
                    "emotion",
                    "Unknown"
                ),

                message=data.get(
                    "message",
                    ""
                )

            )



        except Exception as error:

            print(
                "Concept parsing failed:",
                error
            )


            return self._fallback_concept()





    def _fallback_concept(
        self
    ) -> Concept:


        return Concept(

            theme="Memory",

            emotion="Nostalgia",

            message="Keep the moment"

        )