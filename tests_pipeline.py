from core.events.bus.event_bus import EventBus

from core.application import ExecutionContext

from core.events.models import (
    ProjectCreatedEvent,
    ConceptCreatedEvent
)

from core.agents.runtime import (
    ConceptAgent,
    LyricAgent
)

from core.infrastructure.repositories import (
    SQLiteWorkRepository
)

from core.ai.factory import ProviderFactory

from core.config import settings

from core.ai.runtime import (
    ProviderRegistry,
    AIService
)



def main():


    event_bus = EventBus()


    context = ExecutionContext(
        project_id="pipeline-test"
    )


    provider_registry = ProviderRegistry()


    provider = ProviderFactory.create(
        settings.ai_provider
    )


    provider_registry.register(
        provider
    )


    ai_service = AIService(
        provider_registry,
        settings.ai_provider,
        context
    )


    work_repository = SQLiteWorkRepository(
        settings.database_path
    )


    concept_agent = ConceptAgent(
        event_bus,
        ai_service
    )


    lyric_agent = LyricAgent(
        work_repository,
        ai_service
    )


    event_bus.subscribe(
        ProjectCreatedEvent,
        concept_agent.handle
    )


    event_bus.subscribe(
        ConceptCreatedEvent,
        lyric_agent.handle
    )


    event = ProjectCreatedEvent(
        "pipeline-test"
    )


    event_bus.publish(
        event
    )


    print(
        "\nExecution Summary:"
    )


    print(
        context
    )



if __name__ == "__main__":

    main()