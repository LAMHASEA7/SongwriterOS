from core.domain.models import CreativeProject
from core.domain.repositories import ProjectRepository

from core.application.commands import CreateProjectCommand

from core.events.bus.event_bus import EventBus
from core.events.models import ProjectCreatedEvent


class CreateProjectUseCase:

    def __init__(
        self,
        repository: ProjectRepository,
        event_bus: EventBus
    ):
        self.repository = repository
        self.event_bus = event_bus


    def execute(
        self,
        command: CreateProjectCommand
    ):

        project = CreativeProject(
            title=command.title,
            project_type=command.project_type
        )


        self.repository.save(project)


        event = ProjectCreatedEvent(
            project.id
        )


        self.event_bus.publish(event)


        return project