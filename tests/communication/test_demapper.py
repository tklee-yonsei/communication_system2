import numpy as np
from communication.demapper import Demapper
from tests.communication.test_demapper_interface import demap_and_test

def test_demapper():
    demapper = Demapper()
    data = np.array([-1, -1, 1, 1])
    demapped_data = np.array([0, 0, 1, 1])
    demap_and_test(demapper, data, demapped_data)
