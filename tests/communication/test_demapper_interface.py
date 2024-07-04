import numpy as np

def demap_and_test(
        demapper_interface, data, demapped_data):
    data_with_demap = demapper_interface.demap(data)
    assert np.array_equal(
        data_with_demap, demapped_data)