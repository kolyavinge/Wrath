class LinearRandomGenerator:

    def __init__(self, seed=0):
        self.a = 9459654965476
        self.c = 6745675467549
        self.m = 4643578547845
        self.seed = seed
        self.x = self.seed

    def getSeed(self):
        return self.seed

    def setSeed(self, seed):
        self.seed = seed

    def getFloat(self, left, right):
        self.x = (self.a * self.x + self.c) % self.m
        result = (self.x / self.m) * (right - left) + left

        return result
