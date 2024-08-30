from game.anx.PlayerConstants import PlayerConstants
from game.calc.Line import Line
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.lib.Numeric import Numeric
from game.model.level.Orientation import Orientation


class Wall:

    def __init__(self):
        self.orientation = Orientation.horizontal
        self.startPoint = Vector3()
        self.endPoint = Vector3()
        self.frontNormal = Vector3()
        self.direction = Vector3()
        self.limitLine = Line()
        self.limitLineDirection = Vector3()
        self.checkSegmentVisibility = True
        self.height = 3
        self.info = ""

    def commit(self):
        self.direction = self.startPoint.getDirectionTo(self.endPoint)
        self.upStartPoint = self.startPoint.copy()
        self.upStartPoint.z += self.height
        self.upEndPoint = self.endPoint.copy()
        self.upEndPoint.z += self.height
        self.calculateWallLimitLine()

    def calculateWallLimitLine(self):
        limitLineDirection = self.frontNormal.copy()
        limitLineDirection.setLength(self.getLimitLineOffset())
        self.limitLine.startPoint = self.startPoint.copy()
        self.limitLine.endPoint = self.endPoint.copy()
        self.limitLine.startPoint.add(limitLineDirection)
        self.limitLine.endPoint.add(limitLineDirection)
        self.limitLineDirection = self.limitLine.startPoint.getDirectionTo(self.limitLine.endPoint)

    def getLimitLineOffset(self):
        if self.orientation == Orientation.diagonal:
            return PlayerConstants.xyLengthHalf * Math.sqrt(2)
        else:
            return PlayerConstants.xyLengthHalf

    def getBorderPoints(self):
        return [self.startPoint, self.endPoint, self.upStartPoint, self.upEndPoint]

    def validate(self):
        assert self.startPoint != self.endPoint
        assert self.limitLine.startPoint != self.limitLine.endPoint
        assert Numeric.floatEquals(self.frontNormal.getLength(), 1)
        wallDirection = self.startPoint.getDirectionTo(self.endPoint)
        assert wallDirection.getLength() >= 1
        if self.orientation == Orientation.horizontal:
            assert self.startPoint.y == self.endPoint.y
            assert self.startPoint.x < self.endPoint.x
            assert self.frontNormal == Vector3(0, 1, 0) or self.frontNormal == Vector3(0, -1, 0)
        elif self.orientation == Orientation.vertical:
            assert self.startPoint.x == self.endPoint.x
            assert self.startPoint.y < self.endPoint.y
            assert self.frontNormal == Vector3(1, 0, 0) or self.frontNormal == Vector3(-1, 0, 0)
        else:
            assert self.startPoint.x < self.endPoint.x

    def __str__(self):
        return f"({self.startPoint} - {self.endPoint})"
