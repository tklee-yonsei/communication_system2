from abc import ABC, abstractmethod

class NoiseInterface(ABC):
    @abstractmethod
    def apply(self, signal):
        pass
