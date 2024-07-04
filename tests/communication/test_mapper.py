import numpy as np
from communication.mapper import Mapper
from tests.communication.test_mapper_interface import map_and_test


def test_mapper():
    mapper = Mapper()
    data = np.array([0, 1, 1, 0])
    mapped_data = np.array([-1, 1, 1, -1])
    map_and_test(mapper, data, mapped_data)
    