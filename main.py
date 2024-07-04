import numpy as np

from communication.decoder import Decoder
from communication.demapper import Demapper
from communication.encoder import Encoder
from communication.mapper import Mapper
from communication.receiver import Receiver
from communication.transmitter import Transmitter
from noise.awgn_noise import AWGNNoise
from noise.no_noise import NoNoise

def main():
    data = np.random.randint(0, 2, 100)
    encoder = Encoder()
    mapper = Mapper()
    demapper = Demapper()
    decoder = Decoder()

    transmitter = Transmitter(encoder, mapper)
    receiver = Receiver(decoder, demapper)
    
    print("Test No Noise")
    transmitted_signal = transmitter.transmit(data)
    no_noise = NoNoise()
    noisy_signal = no_noise.apply(transmitted_signal)
    received_data = receiver.receive(noisy_signal)
    print("Original: ", data)
    print("Received: ", received_data)

    print("----------")

    print("Test AWGN Noise")
    transmitted_signal2 = transmitter.transmit(data)
    awgn_noise = AWGNNoise(snr_db=10)
    noisy_signal2 = awgn_noise.apply(transmitted_signal2)
    received_data2 = receiver.receive(noisy_signal2)
    print("Original: ", data)
    print("Received: ", received_data2)

if __name__ == "__main__":
    main()
