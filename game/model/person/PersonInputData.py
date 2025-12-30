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
        self.altFire = False
        self.jump = False

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

    def anyActions(self):
        return (
            self.goForward
            or self.goBackward
            or self.stepLeft
            or self.stepRight
            or self.turnLeftRadians > 0
            or self.turnRightRadians > 0
            or self.lookUpRadians > 0
            or self.lookDownRadians > 0
            or self.fire
            or self.altFire
            or self.jump
        )
