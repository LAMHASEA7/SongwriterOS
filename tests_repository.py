from core.domain.repositories import ProjectRepository
from core.domain.services.project_service import ProjectService


class FakeProjectRepository(ProjectRepository):

    def __init__(self):
        self.projects = []


    def save(self, project):

        self.projects.append(project)


    def find(self, project_id):

        for project in self.projects:

            if project.id == project_id:
                return project

        return None



def main():

    repository = FakeProjectRepository()

    service = ProjectService(repository)


    project = service.create_project(
        "First SongwriterOS Project",
        "Song"
    )


    print(project)

    result = repository.find(project.id)

    print("Found:")
    print(result)



if __name__ == "__main__":
    main()