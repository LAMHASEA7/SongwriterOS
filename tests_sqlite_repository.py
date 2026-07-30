from core.infrastructure.repositories.sqlite_project_repository import (
    SQLiteProjectRepository
)

from core.domain.models import CreativeProject


def main():

    repo = SQLiteProjectRepository(
        "database/songwriteros.db"
    )


    project = CreativeProject(
        title="Infrastructure Test Project",
        project_type="Song"
    )


    repo.save(project)


    print("Saved:")
    print(project)


if __name__ == "__main__":
    main()