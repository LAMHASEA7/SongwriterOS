from core.domain.models import CreativeProject
from core.domain.repositories import ProjectRepository

from core.application.commands import CreateProjectCommand


class CreateProjectUseCase:

    def __init__(
        self,
        repository: ProjectRepository
    ):
        self.repository = repository


    def execute(
        self,
        command: CreateProjectCommand
    ):

        project = CreativeProject(
            title=command.title,
            project_type=command.project_type
        )


        self.repository.save(project)


        return project