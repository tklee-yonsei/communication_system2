import numpy as np

from noise.noise_interface import NoiseInterface

class AWGNNoise(NoiseInterface):
    def __init__(self, snr_db):
        self.snr_db = snr_db

    def apply(self, signal):
        # 데시벨 단위의 SNR 값을 선형 단위로 변환합니다.
        snr_linear = 10 ** (self.snr_db / 10)
        # 신호의 평균 전력 계산
        power_signal = np.mean(np.abs(signal) ** 2)
        # 신호 전력을 SNR로 나누어 노이즈 전력 계산
        noise_power = power_signal / snr_linear

        # 노이즈 생성
        noise = np.sqrt(noise_power / 2) * (
            np.random.randn(*signal.shape) + 
            1j * np.random.randn(*signal.shape)
        )
        # *signal.shape는 python의 unpacking!
        # signal.shape가 (4, 4)라면, *signal.shape는 4, 4로 변환
        return signal + noise
        