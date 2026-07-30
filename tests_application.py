from core.application.use_cases import CreateProjectUseCase
from core.application.commands import CreateProjectCommand

from core.infrastructure.repositories import (
    SQLiteProjectRepository
)


def main():

    repository = SQLiteProjectRepository(
        "database/songwriteros.db"
    )


    use_case = CreateProjectUseCase(
        repository
    )


    command = CreateProjectCommand(
        title="Application Layer Test",
        project_type="Song"
    )


    project = use_case.execute(
        command
    )


    print(project)



if __name__ == "__main__":
    main()