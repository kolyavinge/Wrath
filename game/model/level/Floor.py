from game.calc.Vector3 import Vector3


class Floor:

    def __init__(self):
        self.downLeft = Vector3()
        self.downRight = Vector3()
        self.upLeft = Vector3()
        self.upRight = Vector3()

    def getBorderPoints(self):
        return [self.downLeft, self.downRight, self.upLeft, self.upRight]
