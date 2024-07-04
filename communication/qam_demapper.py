from communication.demapper_interface import DemapperInterface


class QAMDemapper(DemapperInterface):
    def demap(self, data):
        return data