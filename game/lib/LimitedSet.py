class LimitedSet:

    def __init__(self, maxCount):
        self.maxCount = maxCount
        self.listItems = []
        self.setItems = set()

    def append(self, item):
        if len(self.listItems) == self.maxCount:
            first = self.listItems[0]
            self.listItems.remove(first)
            self.setItems.remove(first)

        self.listItems.append(item)
        self.setItems.add(item)

    def getItems(self):
        return self.listItems

    def __contains__(self, item):
        return item in self.setItems

    def clear(self):
        self.listItems.clear()
        self.setItems.clear()

    def __len__(self):
        return len(self.listItems)
