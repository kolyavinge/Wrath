from typing import Sized

# хранит ограниченное кол-во обьектов с возможностью поиска по ключу


class LimitedCollection(Sized):

    def __init__(self, maxCount, getKeyFunc):
        self.maxCount = maxCount
        self.getKeyFunc = getKeyFunc
        self.listItems = []
        self.dictItems = {}

    def append(self, item):
        if len(self.listItems) == self.maxCount:
            first = self.listItems[0]
            self.listItems.remove(first)
            self.dictItems.pop(self.getKeyFunc(first))

        self.listItems.append(item)
        self.dictItems[self.getKeyFunc(item)] = item

    def getByKey(self, key):
        return self.dictItems[key]

    def getItems(self):
        return self.listItems

    def clear(self):
        self.listItems.clear()
        self.dictItems.clear()

    def __len__(self) -> int:
        return len(self.listItems)
