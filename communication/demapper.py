from communication.demapper_interface import DemapperInterface


class Demapper(DemapperInterface):
    def demap(self, data):
        return (data > 0).astype(int)

# 1 or -1
# True or False
# 0 or 1