class AgentStep:


    def __init__(
        self,
        name,
        agent,
        event_factory=None,
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


        if self.event_factory:

            event = self.event_factory(
                execution
            )

        else:

            event = execution.input_event



        result = self.agent.handle(
            event
        )


        #
        # Save result immediately
        #

        if self.output_key:

            execution.state[
                self.output_key
            ] = result



        return result