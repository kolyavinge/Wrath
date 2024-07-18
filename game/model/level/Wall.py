from game.calc.Line import Line
from game.calc.Vector3 import Vector3
from game.lib.Numeric import Numeric
from game.model.level.Orientation import Orientation


class Wall:

    def __init__(self):
        self.orientation = Orientation.horizontal
        self.startPoint = Vector3()
        self.endPoint = Vector3()
        self.frontNormal = Vector3()
        self.crossLine = Line()
        self.crossLineDirection = Vector3()
        self.isPrimary = True
        self.height = 3

    def validate(self):
        assert self.startPoint != self.endPoint
        assert self.crossLine.startPoint != self.crossLine.endPoint
        assert Numeric.floatEquals(self.frontNormal.getLength(), 1)
        wallDirection = self.endPoint.getDirectionTo(self.startPoint)
        assert wallDirection.getLength() >= 1
        if self.orientation == Orientation.horizontal:
            assert self.startPoint.y == self.endPoint.y
            assert self.startPoint.x < self.endPoint.x
            assert self.frontNormal == Vector3(0, 1, 0) or self.frontNormal == Vector3(0, -1, 0)
        elif self.orientation == Orientation.vertical:
            assert self.startPoint.x == self.endPoint.x
            assert self.startPoint.y < self.endPoint.y
            assert self.frontNormal == Vector3(1, 0, 0) or self.frontNormal == Vector3(-1, 0, 0)

    def __str__(self):
        return f"({self.startPoint} - {self.endPoint})"
