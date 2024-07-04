from abc import ABC, abstractmethod

class DemapperInterface(ABC):
    @abstractmethod
    def demap(self, data):
        pass