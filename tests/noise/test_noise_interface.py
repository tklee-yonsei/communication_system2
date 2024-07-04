import numpy as np

from noise.noise_interface import NoiseInterface

def apply_noise_and_test(
    noise_interface: NoiseInterface,
    signal,
    should_equal):
    # 노이즈가 적용된 신호
    noisy_signal = noise_interface.apply(signal)
    # 노이즈가 없는 채널을 통과하는 경우
    if should_equal:
        assert np.array_equal(
            signal, noisy_signal), f"Noise가 서로 다릅니다."
    # 노이즈가 있는 채널을 통과하는 경우
    else:
        assert not np.array_equal(signal, noisy_signal), f"{noise_interface.__class__.__name__} failed."
