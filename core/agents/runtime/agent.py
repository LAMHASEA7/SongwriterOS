from abc import ABC, abstractmethod


class Agent(ABC):

    name = "Base Agent"


    @abstractmethod
    def handle(self, event):

        pass