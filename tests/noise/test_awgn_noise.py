import numpy as np
from noise.awgn_noise import AWGNNoise

def test_awgn_noise():
    """
    AWGN 노이즈가 붙으면, 신호가 바뀌겠죠?
    """
    signal = np.array([1, 2, 3, 4], dtype=np.float32)
    noise = AWGNNoise(snr_db=10)
    noisy_signal = noise.apply(signal)
    assert not np.array_equal(signal, noisy_signal)

def test_awgn_noise_statistics():
    signal = np.ones(10000, dtype=np.float32)
    noise = AWGNNoise(snr_db=10)
    noisy_signal = noise.apply(signal)
    noise_only = noisy_signal - signal
    mean = np.mean(noise_only)
    variance = np.var(noise_only)
    assert abs(mean) < 0.1
    expected_variance = np.mean(np.abs(signal) ** 2) / (10 ** (10 / 10))
    assert abs(variance - expected_variance) < expected_variance * 0.1
