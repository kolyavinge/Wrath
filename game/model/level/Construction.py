from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
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
        self.faceDirection = self.getFaceDirection()
        self.calculateSideNormals()

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

    def inRect(self, point):
        return Plane(self.frontNormal, self.downLeft).containsPoint(point, 0.1) and (
            self.leftSideNormal.dotProduct(self.downLeft.getDirectionTo(point)) >= 0
            and self.rightSideNormal.dotProduct(self.downRight.getDirectionTo(point)) >= 0
            and self.topSideNormal.dotProduct(self.upLeft.getDirectionTo(point)) >= 0
            and self.bottomSideNormal.dotProduct(self.downLeft.getDirectionTo(point)) >= 0
        )

    def calculateSideNormals(self):
        frontNormal = self.frontNormal
        if self.faceDirection == FaceDirection.clockwise:
            frontNormal = frontNormal.copy()
            frontNormal.mul(-1)

        v = self.upLeft.getDirectionTo(self.downLeft)
        self.leftSideNormal = Geometry.rotatePoint(v, frontNormal, CommonConstants.axisOrigin, Math.piHalf)
        self.leftSideNormal.normalize()

        v = self.downRight.getDirectionTo(self.upRight)
        self.rightSideNormal = Geometry.rotatePoint(v, frontNormal, CommonConstants.axisOrigin, Math.piHalf)
        self.rightSideNormal.normalize()

        v = self.upRight.getDirectionTo(self.upLeft)
        self.topSideNormal = Geometry.rotatePoint(v, frontNormal, CommonConstants.axisOrigin, Math.piHalf)
        self.topSideNormal.normalize()

        v = self.downLeft.getDirectionTo(self.downRight)
        self.bottomSideNormal = Geometry.rotatePoint(v, frontNormal, CommonConstants.axisOrigin, Math.piHalf)
        self.bottomSideNormal.normalize()
