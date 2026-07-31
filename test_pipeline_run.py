from core.events.bus.event_bus import EventBus

from core.agents.runtime.dispatcher import AgentDispatcher

from core.agents.runtime.concept_agent import ConceptAgent
from core.agents.runtime.lyric_agent import LyricAgent

from core.events.models import ConceptCreatedEvent


def main():

    event_bus = EventBus()

    dispatcher = AgentDispatcher(
        event_bus
    )


    concept_agent = ConceptAgent(
        event_bus
    )

    lyric_agent = LyricAgent(
        event_bus
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