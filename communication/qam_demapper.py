from communication.demapper_interface import DemapperInterface
import numpy as np

class QAMDemapper(DemapperInterface):
    def __init__(self):
        self.symbol_map = {
            -3 - 3j: (0, 0, 0, 0),
            -3 - 1j: (0, 0, 0, 1),
            -3 + 3j: (0, 0, 1, 0),
            -3 + 1j: (0, 0, 1, 1),

            -1 - 3j: (0, 1, 0, 0),
            -1 - 1j: (0, 1, 0, 1),
            -1 + 3j: (0, 1, 1, 0),
            -1 + 1j: (0, 1, 1, 1),

            3 - 3j: (1, 0, 0, 0),
            3 - 1j: (1, 0, 0, 1),
            3 + 3j: (1, 0, 1, 0),
            3 + 1j: (1, 0, 1, 1),

            1 - 3j: (1, 1, 0, 0),
            1 - 1j: (1, 1, 0, 1),
            1 + 3j: (1, 1, 1, 0),
            1 + 1j: (1, 1, 1, 1),
        }

    def __closest_symbol(self, symbol):
        return min(self.symbol_map.keys(), key=lambda x: np.abs(x - symbol))

    def demap(self, data):
        demapped_data = [self.symbol_map[self.__closest_symbol(symbol)] for symbol in data]
        # ((0, 0, 0, 0), (1, 1, 1, 1))
        # [0, 0, 0, 0, 1, 1, 1, 1]
        return np.array(demapped_data).flatten()

    