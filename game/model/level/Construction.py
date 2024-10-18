from game.calc.RectPlane import RectPlane
from game.calc.Vector3 import Vector3
from game.model.FaceDirection import FaceDirection
from game.model.Visible import Visible


class Construction(Visible):

    def __init__(self):
        super().__init__()
        # глобальные координаты
        self.downLeft = Vector3()
        self.downRight = Vector3()
        self.upLeft = Vector3()
        self.upRight = Vector3()
        self.frontNormal = Vector3()
        # координаты относительно фронтальной грани (frontNormal)
        self.frontDownLeft = Vector3()
        self.frontDownRight = Vector3()
        self.frontUpLeft = Vector3()
        self.frontUpRight = Vector3()

    def commit(self):
        self.faceDirection = self.getFaceDirection()
        self.calculateFrontCoords()
        self.plane = RectPlane(self.frontNormal, self.frontDownLeft, self.frontDownRight, self.frontUpLeft, self.frontUpRight)

    def getFaceDirection(self):
        v = self.downLeft.getDirectionTo(self.downRight)
        v1 = self.downLeft.getDirectionTo(self.upRight)
        v.vectorProduct(v1)
        if v.dotProduct(self.frontNormal) > 0.0:
            return FaceDirection.counterClockwise
        else:
            return FaceDirection.clockwise

    def getBorderPoints(self):
        return [self.downLeft, self.downRight, self.upLeft, self.upRight]

    def containsPoint(self, point):
        return self.plane.containsPoint(point, 0.1)

    def calculateFrontCoords(self):
        if self.faceDirection == FaceDirection.counterClockwise:
            self.frontDownLeft = self.downLeft
            self.frontDownRight = self.downRight
            self.frontUpLeft = self.upLeft
            self.frontUpRight = self.upRight
        else:
            self.frontDownLeft = self.downRight
            self.frontDownRight = self.downLeft
            self.frontUpLeft = self.upRight
            self.frontUpRight = self.upLeft
