class TimeLimitedItem:

    def __init__(self, innerItem, timeLimit):
        self.innerItem = innerItem
        self.timeLimit = timeLimit

    def __str__(self):
        return f"{self.innerItem}:{self.timeLimit}"


class TimeLimitedCollectionIterator:

    def __init__(self, items):
        self.items = items
        self.length = len(items)
        self.currentIndex = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.currentIndex < self.length:
            item = self.items[self.currentIndex].innerItem
            self.currentIndex += 1
            return item
        else:
            raise StopIteration()


# хранит элементы определенное время, потом удаляет те, для которых оно истекло
class TimeLimitedCollection:

    def __init__(self, timeLimit):
        self.timeLimit = timeLimit
        self.items = []

    def append(self, item):
        self.items.append(TimeLimitedItem(item, self.timeLimit))

    def deleteTimeLimitedItems(self):
        if len(self.items) == 0:
            return

        needDelete = False
        for item in self.items:
            item.timeLimit -= 1
            needDelete = needDelete or item.timeLimit == 0

        if needDelete:
            self.items = [item for item in self.items if item.timeLimit > 0]

    def __iter__(self):
        return TimeLimitedCollectionIterator(self.items)

    def __len__(self):
        return len(self.items)
