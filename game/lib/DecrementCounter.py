class DecrementCounter:

    def __init__(self, minValue=0):
        self.minValue = minValue
        self.value = minValue

    def set(self, value):
        self.value = value

    def decrease(self):
        if self.value > self.minValue:
            self.value -= 1

    def isExpired(self):
        return self.value == self.minValue
