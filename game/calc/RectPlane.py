from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.lib.Math import Math


class RectPlane(Plane):

    def __init__(self, normal, downLeft, downRight, upLeft, upRight):
        super().__init__(normal, downLeft)
        self.normal = normal
        self.downLeft = downLeft
        self.downRight = downRight
        self.upLeft = upLeft
        self.upRight = upRight
        self.calculateSideNormals()

    def containsPoint(self, point, eps=0.0001):
        return super().containsPoint(point, eps) and (
            self.leftSideNormal.dotProduct(self.downLeft.getDirectionTo(point)) >= 0
            and self.rightSideNormal.dotProduct(self.downRight.getDirectionTo(point)) >= 0
            and self.topSideNormal.dotProduct(self.upLeft.getDirectionTo(point)) >= 0
            and self.bottomSideNormal.dotProduct(self.downLeft.getDirectionTo(point)) >= 0
        )

    def calculateSideNormals(self):
        v = self.upLeft.getDirectionTo(self.downLeft)
        self.leftSideNormal = Geometry.rotatePoint(v, self.normal, CommonConstants.axisOrigin, Math.piHalf)
        self.leftSideNormal.normalize()

        v = self.downRight.getDirectionTo(self.upRight)
        self.rightSideNormal = Geometry.rotatePoint(v, self.normal, CommonConstants.axisOrigin, Math.piHalf)
        self.rightSideNormal.normalize()

        v = self.upRight.getDirectionTo(self.upLeft)
        self.topSideNormal = Geometry.rotatePoint(v, self.normal, CommonConstants.axisOrigin, Math.piHalf)
        self.topSideNormal.normalize()

        v = self.downLeft.getDirectionTo(self.downRight)
        self.bottomSideNormal = Geometry.rotatePoint(v, self.normal, CommonConstants.axisOrigin, Math.piHalf)
        self.bottomSideNormal.normalize()
