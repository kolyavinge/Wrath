import random


class Random:

    @staticmethod
    def getInt(left, right):
        return random.randint(left, right)

    @staticmethod
    def getFloat(left, right):
        return random.uniform(left, right)

    @staticmethod
    def getBool():
        return Random.getInt(1, 100) % 2 == 0

    @staticmethod
    def getListItem(lst):
        return lst[Random.getInt(0, len(lst) - 1)]
