from core.events.event import Event


class ProjectCreatedEvent(Event):

    def __init__(
        self,
        project_id
    ):

        super().__init__()

        self.project_id = project_id