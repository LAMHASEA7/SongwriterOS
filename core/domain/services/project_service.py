from ..models.project import CreativeProject


class ProjectService:


    def __init__(self, repository):

        self.repository = repository



    def create_project(self, title, project_type):

        project = CreativeProject(
            title=title,
            project_type=project_type
        )

        self.repository.save(project)

        return project