class AgentRegistry:


    def __init__(self):

        self.agents = []


    def register(
        self,
        agent
    ):

        self.agents.append(agent)


    def all(self):

        return self.agents