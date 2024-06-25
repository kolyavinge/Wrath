from game.calc.Line import Line
from game.calc.Vector3 import Vector3
from game.model.level.Orientation import Orientation


class Wall:

    def __init__(self):
        self.orientation = Orientation.horizontal
        self.startPoint = Vector3()
        self.endPoint = Vector3()
        self.frontNormal = Vector3()
        self.crossLine = Line()

    def getMinX(self):
        return min(self.startPoint.x, self.endPoint.x)

    def getMaxX(self):
        return max(self.startPoint.x, self.endPoint.x)

    def getMinY(self):
        return min(self.startPoint.y, self.endPoint.y)

    def getMaxY(self):
        return max(self.startPoint.y, self.endPoint.y)

    def validate(self):
        self.check(self.orientation == Orientation.horizontal or self.orientation == Orientation.vertical)
        self.check(self.startPoint != self.endPoint)
        self.check(self.crossLine.startPoint != self.crossLine.endPoint)
        self.check(self.frontNormal.getLength() == 1)
        wallDirection = self.endPoint.getCopy()
        wallDirection.sub(self.startPoint)
        self.check(wallDirection.getLength() == int(wallDirection.getLength()))
        if self.orientation == Orientation.horizontal:
            self.check(self.startPoint.y == self.endPoint.y)
            self.check(self.startPoint.x < self.endPoint.x)
            self.check(self.frontNormal == Vector3(0, 1, 0) or self.frontNormal == Vector3(0, -1, 0))
        elif self.orientation == Orientation.vertical:
            self.check(self.startPoint.x == self.endPoint.x)
            self.check(self.startPoint.y < self.endPoint.y)
            self.check(self.frontNormal == Vector3(1, 0, 0) or self.frontNormal == Vector3(-1, 0, 0))

    def check(self, value):
        if value == False:
            raise Exception()

    def toString(self):
        return f"({self.startPoint.toString()}-{self.endPoint.toString()})"

    def __str__(self):
        return self.toString()
