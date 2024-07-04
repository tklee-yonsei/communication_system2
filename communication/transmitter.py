class Transmitter:
    def __init__(self, encoder, mapper):
        self.encoder = encoder
        self.mapper = mapper
    
    def transmit(self, data):
        encoded_data = self.encoder.encode(data)
        mapped_data = self.mapper.map(encoded_data)
        return mapped_data