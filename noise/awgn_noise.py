from noise.noise_interface import NoiseInterface

class AWGNNoise(NoiseInterface):
    def __init__(self, snr_db):
        self.snr_db = snr_db

    def apply(self, signal):
        return signal + 1
        