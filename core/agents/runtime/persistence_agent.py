from core.agents.runtime.agent import Agent

from core.domain.models import CreativeWork


class PersistenceAgent(Agent):

    name = "Persistence Agent"


    def __init__(
        self,
        project_repository,
        lyrics_repository,
        work_repository,
        context
    ):

        self.project_repository = project_repository

        self.lyrics_repository = lyrics_repository

        self.work_repository = work_repository

        self.context = context



    def handle(
        self,
        event
    ):

        song_project = self.context.song_project


        if song_project is None:

            return None



        #
        # Save Project
        #

        self.project_repository.save(
            song_project
        )



        #
        # Save Lyrics Work
        #

        if song_project.lyrics:


            self.work_repository.save(
                song_project.lyrics,
                project_id=str(
                    song_project.id
                )
            )


            self.lyrics_repository.save(
                song_project.lyrics,
                song_id=str(
                    song_project.id
                )
            )



        print(
            f"Project persisted: {song_project.title}"
        )


        return song_project