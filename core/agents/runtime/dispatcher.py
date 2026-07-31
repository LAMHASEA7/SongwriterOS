class AgentDispatcher:

    def __init__(self, event_bus):

        self.event_bus = event_bus


    def register(
        self,
        event_type,
        agent
    ):

        self.event_bus.subscribe(
            event_type,
            agent.handle
        )