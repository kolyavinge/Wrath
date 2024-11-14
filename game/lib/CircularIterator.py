class CircularIterator:

    def __init__(self, items):
        self.items = items
        self.index = 0
        self.length = len(self.items)

    def move(self):
        self.index += 1
        if self.index == self.length:
            self.index = 0

    def getItem(self):
        return self.items[self.index]
