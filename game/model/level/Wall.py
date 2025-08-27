from game.anx.PersonConstants import PersonConstants
from game.calc.Line import Line
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.lib.Numeric import Numeric
from game.model.level.Construction import Construction
from game.model.Orientation import Orientation


class Wall(Construction):

    def __init__(self):
        super().__init__()
        self.orientation = None
        self.startPoint = Vector3()
        self.endPoint = Vector3()
        self.startPointHeight = 3.0
        self.endPointHeight = 3.0
        self.direction = Vector3()
        self.limitLine = Line()
        self.limitLineDirection = Vector3()
        self.info = ""
        self.visualSize = 2.0

    def commit(self):
        self.downLeft = self.startPoint
        self.downRight = self.endPoint
        self.upLeft = self.startPoint.copy()
        self.upLeft.z += self.startPointHeight
        self.upRight = self.endPoint.copy()
        self.upRight.z += self.endPointHeight
        super().commit()
        self.direction = self.startPoint.getDirectionTo(self.endPoint)
        self.calculateOrientation()
        self.calculateWallLimitLine()

    def calculateOrientation(self):
        if self.startPoint.y == self.endPoint.y:
            self.orientation = Orientation.horizontal
        elif self.startPoint.x == self.endPoint.x:
            self.orientation = Orientation.vertical
        else:
            self.orientation = Orientation.diagonal

    def calculateWallLimitLine(self):
        limitLineOffset = self.frontNormal.copy()
        limitLineOffset.setLength(self.getLimitLineOffset())
        self.limitLine.startPoint = self.startPoint.copy()
        self.limitLine.endPoint = self.endPoint.copy()
        self.limitLine.startPoint.add(limitLineOffset)
        self.limitLine.endPoint.add(limitLineOffset)
        limitLineTail = self.limitLine.startPoint.getDirectionTo(self.limitLine.endPoint)
        limitLineTail.setLength(2)
        self.limitLine.startPoint.sub(limitLineTail)
        self.limitLine.endPoint.add(limitLineTail)
        self.limitLineDirection = self.limitLine.startPoint.getDirectionTo(self.limitLine.endPoint)

    def getLimitLineOffset(self):
        if self.orientation == Orientation.diagonal:
            return PersonConstants.xyLengthHalf * Math.sqrt(2) + 0.1
        else:
            return PersonConstants.xyLengthHalf + 0.1

    def validate(self):
        assert self.startPoint != self.endPoint
        assert self.limitLine.startPoint != self.limitLine.endPoint
        assert Numeric.floatEquals(self.frontNormal.getLength(), 1)

    def __str__(self):
        return f"({self.startPoint} - {self.endPoint})"
