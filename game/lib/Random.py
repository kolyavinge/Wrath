import random


class Random:

    def __init__(self):
        random.seed()

    def getFloat(self, left, right):
        return random.uniform(left, right)
