from core.events.bus.event_bus import EventBus
from core.events.models import (
    ProjectCreatedEvent,
    ArrangementCreatedEvent
)

from core.domain.song_project import SongProject

from core.agents.runtime import (
    ConceptAgent,
    LyricAgent,
    MelodyAgent,
    ArrangementAgent
)


from core.infrastructure.repositories import (
    SQLiteWorkRepository,
    SQLiteProjectRepository,
    SQLiteSongRepository,
    SQLiteLyricsRepository
)


from core.workflow.song_creation import SongCreationWorkflow
from core.workflow.engine import WorkflowEngine


from core.ai.factory import ProviderFactory

from core.ai.runtime import (
    ProviderRegistry,
    AIService
)


from core.config import settings

from core.application import ExecutionContext


from core.events.subscribers.persistence_subscriber import (
    PersistenceSubscriber
)



def main():

    print("START TEST")



    #
    # Event Bus
    #

    event_bus = EventBus()



    #
    # Execution Context
    #

    context = ExecutionContext(
        project_id="workflow-test"
    )



    song_project = SongProject(
        title="Lost Memories"
    )



    context.attach_project(
        song_project
    )



    #
    # Repository
    #

    work_repository = SQLiteWorkRepository(
        settings.database_path
    )


    project_repository = SQLiteProjectRepository(
        settings.database_path
    )

    song_repository = SQLiteSongRepository(
        settings.database_path
    )

    lyrics_repository = SQLiteLyricsRepository(
        settings.database_path
    )



    #
    # Persistence Subscriber
    #

    persistence_subscriber = PersistenceSubscriber(

        project_repository,

        song_repository,

        lyrics_repository,

        work_repository,

        context

    )


    event_bus.subscribe(

        ArrangementCreatedEvent,

        persistence_subscriber.handle

    )



    #
    # AI Setup
    #

    registry = ProviderRegistry()



    provider = ProviderFactory.create(
        settings.ai_provider
    )



    registry.register(
        provider
    )



    ai_service = AIService(
        registry,
        settings.ai_provider,
        context
    )



    #
    # Agents
    #

    concept_agent = ConceptAgent(

        event_bus,

        ai_service,

        context

    )



    lyric_agent = LyricAgent(

        event_bus,

        ai_service,

        context

    )



    melody_agent = MelodyAgent(

        event_bus,

        context

    )



    arrangement_agent = ArrangementAgent(

        event_bus,

        context

    )



    #
    # Workflow
    #

    workflow_builder = SongCreationWorkflow(

        concept_agent,

        lyric_agent,

        melody_agent,

        arrangement_agent,

        event_bus

    )



    workflow = workflow_builder.build()



    #
    # Execute
    #

    engine = WorkflowEngine()



    event = ProjectCreatedEvent(
        "workflow-test"
    )



    result = engine.execute(

        workflow,

        event

    )



    print()


    print(
        "Workflow Status:",
        result.status
    )



    print()


    print(
        "JSON RESULT:"
    )



    print(
        result.to_json()
    )



    print()


    print(
        "Workflow History:"
    )



    for item in result.history:

        print(
            item
        )




if __name__ == "__main__":

    main()