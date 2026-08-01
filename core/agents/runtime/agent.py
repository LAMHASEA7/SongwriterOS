from abc import ABC, abstractmethod


class Agent(ABC):

    name = "Base Agent"

    capability = None


    def __init__(
        self,
        context=None
    ):

        self.context = context



    def register_execution(
        self
    ):

        if self.context:

            self.context.register_agent(
                self.name
            )



    def emit_event(
        self,
        event_name
    ):

        if self.context:

            self.context.register_event(
                event_name
            )



    def log(
        self,
        message
    ):

        print(
            f"[{self.name}] {message}"
        )



    @abstractmethod
    def handle(
        self,
        event
    ):

        pass