from abc import ABC, abstractmethod


class AIProvider(ABC):

    name = "Base Provider"

    @abstractmethod
    def generate(
        self,
        prompt
    ):
        pass