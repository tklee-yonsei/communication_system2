import numpy as np
from communication.qam_mapper import QAMMapper
from tests.communication.test_mapper_interface import map_and_test


def test_qam_mapper():
    mapper = QAMMapper()
    data = np.array([
        0, 0, 0, 0, 1, 1, 1, 1
    ])
    mapped_data = np.array([
        -3 - 3j,
        1 + 1j
    ])
    map_and_test(
        mapper,
        data,
        mapped_data)