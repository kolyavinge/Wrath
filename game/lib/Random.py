import random


class Random:

    def getInt(self, left, right):
        return random.randint(left, right - 1)

    def getFloat(self, left, right):
        return random.uniform(left, right)
