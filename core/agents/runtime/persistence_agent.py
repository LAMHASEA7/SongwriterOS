from core.agents.runtime.agent import Agent


class PersistenceAgent(Agent):

    name = "Persistence Agent"

    def __init__(
        self,
        repository,
        context
    ):
        self.repository = repository
        self.context = context

    def handle(self, event):

        song = self.context.song_project

        self.repository.save(song)

        print(
            f"Project saved: {song.title}"
        )

        return song