from noise.noise_interface import NoiseInterface

class NoNoise(NoiseInterface):
    def apply(self, signal):
        raise NotImplementedError("NoNoise 메소드 구현 필요")
        