from game.calc.Vector3 import Vector3
from game.model.level.Orientation import Orientation


class SplitLine:

    def __init__(self):
        self.priority = 0
        self.startPoint = Vector3()
        self.endPoint = Vector3()
        self.frontNormal = Vector3()
        self.orientation = Orientation.horizontal
        self.orientationCanChange = True
        self.sortOrder = 0

    def toString(self):
        return f"({self.startPoint}), ({self.endPoint}), ({self.frontNormal})"

    def __str__(self):
        return self.toString()
