from core.agents.runtime.agent import Agent


class ConceptAgent(Agent):

    name = "Concept Agent"


    def handle(self, event):

        print(
            "Concept Agent processing project:",
            event.project_id
        )