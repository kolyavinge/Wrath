import random


class Random:

    def getInt(self, left, right):
        return random.randint(left, right)

    def getFloat(self, left, right):
        return random.uniform(left, right)

    def getBool(self):
        return self.getInt(1, 100) % 2 == 0
