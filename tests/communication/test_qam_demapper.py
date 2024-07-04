import numpy as np

from communication.qam_demapper import QAMDemapper
from tests.communication.test_demapper_interface import demap_and_test

def test_qam_demapper():
    demapper = QAMDemapper()
    data = np.array([-3 - 3j, 1 + 1j])
    demapped_data = np.array([
        0, 0, 0, 0, 1, 1, 1, 1
    ])
    demap_and_test(demapper, data, demapped_data)