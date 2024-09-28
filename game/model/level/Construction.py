from game.calc.Vector3 import Vector3
from game.model.FaceDirection import FaceDirection
from game.model.Visible import Visible


class Construction(Visible):

    def __init__(self):
        super().__init__()
        self.downLeft = Vector3()
        self.downRight = Vector3()
        self.upLeft = Vector3()
        self.upRight = Vector3()
        self.frontNormal = Vector3()

    def commit(self):
        self.calculateFaceDirection()

    def calculateFaceDirection(self):
        v = self.downLeft.getDirectionTo(self.downRight)
        v1 = self.downLeft.getDirectionTo(self.upRight)
        v.vectorProduct(v1)
        if v.dotProduct(self.frontNormal) > 0.0:
            self.faceDirection = FaceDirection.counterClockwise
        else:
            self.faceDirection = FaceDirection.clockwise

    def getBorderPoints(self):
        return [self.downLeft, self.downRight, self.upLeft, self.upRight]
