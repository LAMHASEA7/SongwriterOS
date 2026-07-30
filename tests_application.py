from core.application.use_cases import CreateProjectUseCase
from core.application.commands import CreateProjectCommand

from core.events.bus.event_bus import EventBus
from core.events.models import ProjectCreatedEvent

from core.audit.subscribers import ProjectCreatedSubscriber

from core.infrastructure.repositories import (
    SQLiteProjectRepository
)


def main():

    repository = SQLiteProjectRepository(
        "database/songwriteros.db"
    )


    event_bus = EventBus()


    audit = ProjectCreatedSubscriber()


    event_bus.subscribe(
        ProjectCreatedEvent,
        audit.handle
    )


    use_case = CreateProjectUseCase(
        repository,
        event_bus
    )


    command = CreateProjectCommand(
        title="Application Event Test",
        project_type="Song"
    )


    project = use_case.execute(
        command
    )


    print(project)



if __name__ == "__main__":
    main()