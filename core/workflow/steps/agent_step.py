class AgentStep:

    def __init__(
        self,
        name,
        agent,
        event_factory,
        output_key=None
    ):

        self.name = name
        self.agent = agent
        self.event_factory = event_factory
        self.output_key = output_key


    def __call__(
        self,
        execution
    ):

        event = self.event_factory(
            execution
        )

        result = self.agent.handle(
            event
        )


        if self.output_key:

            execution.state[
                self.output_key
            ] = result


        return result