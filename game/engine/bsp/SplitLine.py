from game.calc.Vector3 import Vector3


class SplitLine:

    def __init__(self):
        self.priority = 0
        self.startPoint = Vector3()
        self.endPoint = Vector3()
        self.frontNormal = Vector3()
        self.sortOrder = 0
