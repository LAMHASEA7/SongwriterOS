class AgentDispatcher:


    def __init__(
        self,
        registry
    ):

        self.registry = registry



    def handle(
        self,
        event
    ):

        for agent in self.registry.all():

            agent.handle(event)