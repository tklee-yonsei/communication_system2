from noise.noise_interface import NoiseInterface

class NoNoise(NoiseInterface):
    def apply(self, signal):
        return signal
        