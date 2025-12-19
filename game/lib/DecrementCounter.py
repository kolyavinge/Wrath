class DecrementCounter:

    def __init__(self, value=0):
        self.set(value)

    def set(self, value):
        self.initValue = value
        self.value = value

    def reset(self):
        self.value = self.initValue

    def decrease(self):
        if self.value > 0:
            self.value -= 1

    def isFull(self):
        return self.value == self.initValue

    def isExpired(self):
        return self.value == 0
