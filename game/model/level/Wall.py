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
        self.crossLine = Line()
        self.crossLineDirection = Vector3()
        self.collisionLine = Line()
        self.collisionLineDirection = Vector3()
        self.checkSegmentVisibility = True
        self.height = 3
        self.info = ""

    def commit(self):
        self.direction = self.startPoint.getDirectionTo(self.endPoint)
        self.upStartPoint = self.startPoint.copy()
        self.upStartPoint.z += self.height
        self.upEndPoint = self.endPoint.copy()
        self.upEndPoint.z += self.height
        self.calculateWallCrossLine()
        self.calculateCollisionLine()

    def calculateWallCrossLine(self):
        crossDirection = self.frontNormal.copy()
        crossDirection.setLength(self.getCrossLineWallOffset())
        self.crossLine.startPoint = self.startPoint.copy()
        self.crossLine.endPoint = self.endPoint.copy()
        self.crossLine.startPoint.add(crossDirection)
        self.crossLine.endPoint.add(crossDirection)
        self.crossLineDirection = self.crossLine.startPoint.getDirectionTo(self.crossLine.endPoint)

    def calculateCollisionLine(self):
        self.collisionLine.startPoint = self.startPoint.copy()
        self.collisionLine.endPoint = self.endPoint.copy()
        delta = self.direction.copy()
        delta.setLength(0.1)
        self.collisionLine.startPoint.sub(delta)
        self.collisionLine.endPoint.add(delta)
        self.collisionLineDirection = self.collisionLine.startPoint.getDirectionTo(self.collisionLine.endPoint)

    def getCrossLineWallOffset(self):
        if self.orientation == Orientation.diagonal:
            return PlayerConstants.xyLengthHalf * Math.sqrt(2)
        else:
            return PlayerConstants.xyLengthHalf

    def getBorderPoints(self):
        return [self.startPoint, self.endPoint, self.upStartPoint, self.upEndPoint]

    def validate(self):
        assert self.startPoint != self.endPoint
        assert self.crossLine.startPoint != self.crossLine.endPoint
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
