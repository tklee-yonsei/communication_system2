from abc import ABC, abstractmethod

class MapperInterface(ABC):
    @abstractmethod
    def map(self, data):
        pass
