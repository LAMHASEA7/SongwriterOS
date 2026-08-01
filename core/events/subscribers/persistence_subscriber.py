from core.events.models import ArrangementCreatedEvent


class PersistenceSubscriber:


    def __init__(
        self,
        project_repository,
        song_repository,
        lyrics_repository,
        work_repository,
        context
    ):

        self.project_repository = project_repository

        self.song_repository = song_repository

        self.lyrics_repository = lyrics_repository

        self.work_repository = work_repository

        self.context = context



    def handle(
        self,
        event
    ):

        print(
            "PersistenceSubscriber received: ArrangementCreatedEvent"
        )


        project = self.context.song_project


        if project is None:

            print(
                "Persistence skipped: no project"
            )

            return



        #
        # Save Project
        #

        self.project_repository.save(
            project
        )



        #
        # Save Song
        #

        song = project


        self.song_repository.save(
            song,
            event.project_id
        )



        #
        # Save Lyrics
        #

        if project.lyrics:

            self.lyrics_repository.save(
                project.lyrics,
                event.project_id
            )



        #
        # Save Work
        #

        if project.lyrics:

            self.work_repository.save(
                project.lyrics
            )



        print(
            "Persistence completed"
        )