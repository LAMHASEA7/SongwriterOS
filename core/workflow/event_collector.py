class WorkflowEventCollector:


    def __init__(self, execution):

        self.execution = execution


    def handle(
        self,
        event
    ):

        event_name = type(event).__name__

        print(
            f"COLLECT: {event_name}"
        )


        if hasattr(event, "work"):

            self.execution.state[
                "lyrics"
            ] = event.work


        if hasattr(event, "concept"):

            self.execution.state[
                "concept"
            ] = event.concept


        if hasattr(event, "melody"):

            self.execution.state[
                "melody"
            ] = event.melody


        if hasattr(event, "arrangement"):

            self.execution.state[
                "arrangement"
            ] = event.arrangement