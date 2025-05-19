class PersonInputData:

    def __init__(self):
        self.clear()

    def clear(self):
        self.goForward = False
        self.goBackward = False
        self.stepLeft = False
        self.stepRight = False
        self.turnLeftRadians = 0
        self.turnRightRadians = 0
        self.lookUpRadians = 0
        self.lookDownRadians = 0
        self.fire = False

    def setGoForward(self):
        self.goForward = True
        return self

    def setGoBackward(self):
        self.goBackward = True
        return self

    def setStepLeft(self):
        self.stepLeft = True
        return self

    def setStepRight(self):
        self.stepRight = True
        return self
