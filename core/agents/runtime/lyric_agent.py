from core.agents.runtime.agent import Agent


class LyricAgent(Agent):

    name = "Lyric Agent"


    def handle(self, event):

        print(
            "Lyric Agent processing project:",
            event.project_id
        )