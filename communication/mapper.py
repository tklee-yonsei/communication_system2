from communication.mapper_interface import MapperInterface

# class Mapper:
#     def map(self, data):
#         return 2 * data - 1
    
# 0 or 1
# 1 or -1

class Mapper(MapperInterface):
    def map(self, data):
        return 2 * data - 1
