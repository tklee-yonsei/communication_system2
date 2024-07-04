import numpy as np

def map_and_test(mapper_interface, data, mapped_data):
    data_with_map = mapper_interface.map(data)
    assert np.array_equal(data_with_map, mapped_data)