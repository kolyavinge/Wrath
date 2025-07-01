class DecrementCounter:

    def __init__(self):
        self.value = 0

    def set(self, value):
        self.value = value

    def decrease(self):
        if self.value > 0:
            self.value -= 1

    def isExpired(self):
        return self.value == 0
