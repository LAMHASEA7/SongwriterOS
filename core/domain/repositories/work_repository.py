from abc import ABC, abstractmethod


class WorkRepository(ABC):

    @abstractmethod
    def save(self, work):
        pass


    @abstractmethod
    def find(self, work_id):
        pass