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

    def getMinX(self):
        return min(self.startPoint.x, self.endPoint.x)

    def getMaxX(self):
        return max(self.startPoint.x, self.endPoint.x)

    def getMinY(self):
        return min(self.startPoint.y, self.endPoint.y)

    def getMaxY(self):
        return max(self.startPoint.y, self.endPoint.y)

    def __str__(self):
        return f"({self.priority}:{self.startPoint}),({self.endPoint})"
