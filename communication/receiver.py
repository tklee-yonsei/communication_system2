from communication.demapper_interface import DemapperInterface


class Receiver:
    def __init__(self, decoder, demapper: DemapperInterface):
        self.decoder = decoder
        self.demapper = demapper
    
    def receive(self, data):
        demapped_data = self.demapper.demap(data)
        decoded_data = self.decoder.decode(demapped_data)
        return decoded_data