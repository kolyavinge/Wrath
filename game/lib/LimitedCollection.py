# хранит ограниченное кол-во элементов с возможностью поиска по ключу
class LimitedCollection:

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

    def getByKeyOrNone(self, key):
        if key in self.dictItems:
            return self.dictItems[key]
        else:
            return None

    def getItems(self):
        return self.listItems

    def clear(self):
        self.listItems.clear()
        self.dictItems.clear()

    def __len__(self):
        return len(self.listItems)
