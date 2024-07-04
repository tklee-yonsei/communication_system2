import numpy as np

from noise.no_noise import NoNoise
from tests.noise.test_noise_interface import apply_noise_and_test

def test_no_noise():
    signal = np.array([1, 2, 3, 4])
    noise = NoNoise()
    apply_noise_and_test(noise, signal, True)
