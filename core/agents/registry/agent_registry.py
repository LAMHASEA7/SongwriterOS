class AgentRegistry:

    def __init__(self):

        self.agents = {}


    def register(
        self,
        agent
    ):

        capability = agent.capability

        if capability not in self.agents:

            self.agents[capability] = []

        self.agents[capability].append(
            agent
        )


    def get(
        self,
        capability
    ):

        agents = self.agents.get(
            capability,
            []
        )

        if not agents:
            return None

        return agents[0]


    def get_all(
        self,
        capability
    ):

        return self.agents.get(
            capability,
            []
        )


    def all(self):

        return self.agents