from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.Plane import Plane
from game.calc.Vector3 import Vector3
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

    def containsPoint(self, point, eps):
        return super().containsPoint(point, eps) and self.withinBorder(point)

    def withinBorder(self, point):
        return (
            Vector3.calcDirectionAndGetDotProduct(self.downLeft, point, self.leftSideNormal) >= 0
            and Vector3.calcDirectionAndGetDotProduct(self.downRight, point, self.rightSideNormal) >= 0
            and Vector3.calcDirectionAndGetDotProduct(self.upLeft, point, self.topSideNormal) >= 0
            and Vector3.calcDirectionAndGetDotProduct(self.downLeft, point, self.bottomSideNormal) >= 0
        )

    def calculateSideNormals(self):
        v = self.upLeft.getDirectionTo(self.downLeft)
        self.leftSideNormal = Geometry.rotatePoint(v, self.normal, CommonConstants.axisOrigin, Math.piHalf)
        self.leftSideNormal.normalize()
        self.leftSideNormal.roundToZero()

        v = self.downRight.getDirectionTo(self.upRight)
        self.rightSideNormal = Geometry.rotatePoint(v, self.normal, CommonConstants.axisOrigin, Math.piHalf)
        self.rightSideNormal.normalize()
        self.rightSideNormal.roundToZero()

        v = self.upRight.getDirectionTo(self.upLeft)
        self.topSideNormal = Geometry.rotatePoint(v, self.normal, CommonConstants.axisOrigin, Math.piHalf)
        self.topSideNormal.normalize()
        self.topSideNormal.roundToZero()

        v = self.downLeft.getDirectionTo(self.downRight)
        self.bottomSideNormal = Geometry.rotatePoint(v, self.normal, CommonConstants.axisOrigin, Math.piHalf)
        self.bottomSideNormal.normalize()
        self.bottomSideNormal.roundToZero()
