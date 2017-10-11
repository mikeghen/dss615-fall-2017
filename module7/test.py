class Mapping:

    _private_var = "hello"

    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

mapping = Mapping([1,2,3])

msc = MappingSubclass(['hello','good'])

mapping._private_var
msc.__update([1,2,3])
