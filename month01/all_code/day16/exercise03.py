"""

"""


class CommodityIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        if self.__index == len(self.__data) - 1:
            raise StopIteration()
        self.__index += 1
        return self.__data[self.__index]


class CommodityController:
    def __init__(self):
        self.__list_commodity = []

    def add_commodity(self, cmd):
        self.__list_commodity.append(cmd)

    def __iter__(self):
        return CommodityIterator(self.__list_commodity)


controller = CommodityController()
controller.add_commodity("屠龙刀")
controller.add_commodity("倚天剑")
controller.add_commodity("芭比娃娃")
# for item in controller:
#     print(item)
iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
