class PlayerInputData:

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
        self.torchSwitch = False
