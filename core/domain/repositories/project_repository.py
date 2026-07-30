from abc import ABC, abstractmethod


class ProjectRepository(ABC):

    @abstractmethod
    def save(self, project):
        pass


    @abstractmethod
    def find(self, project_id):
        pass