from communication.demapper_interface import DemapperInterface
import numpy as np

class QAMDemapper(DemapperInterface):
    def demap(self, data):
        symbol_map = {
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
        demapped_data = [symbol_map[symbol] for symbol in data]
        # ((0, 0, 0, 0), (1, 1, 1, 1))
        # [0, 0, 0, 0, 1, 1, 1, 1]
        return np.array(demapped_data).flatten()