from core.events.bus.event_bus import EventBus

from core.agents.runtime.dispatcher import AgentDispatcher

from core.agents.runtime.concept_agent import ConceptAgent
from core.agents.runtime.lyric_agent import LyricAgent

from core.events.models import ConceptCreatedEvent

from core.ai.factory import ProviderFactory

from core.infrastructure.repositories.sqlite_work_repository import SQLiteWorkRepository

from core.config import settings


def main():

    event_bus = EventBus()


    ai_provider = ProviderFactory.create(
        "openai"
    )


    work_repository = SQLiteWorkRepository(
        settings.database_path
    )


    dispatcher = AgentDispatcher(
        event_bus
    )


    concept_agent = ConceptAgent(
        event_bus,
        ai_provider
    )


    lyric_agent = LyricAgent(
        work_repository,
        ai_provider
    )


    dispatcher.register(
        ConceptCreatedEvent,
        lyric_agent
    )


    concept_agent.handle(
        None
    )


if __name__ == "__main__":

    main()