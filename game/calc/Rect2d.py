from game.calc.Vector3 import Vector3
from game.lib.Numeric import Numeric


class Rect2d:

    def __init__(self, xLength, yLength):
        self.xLength = xLength
        self.yLength = yLength
        self.xLengthHalf = xLength / 2
        self.yLengthHalf = yLength / 2
        self.center = Vector3()
        self.downLeft = Vector3()
        self.downRight = Vector3()
        self.upLeft = Vector3()
        self.upRight = Vector3()
        self.middleLeft = Vector3()
        self.middleRight = Vector3()
        self.middleTop = Vector3()
        self.middleBottom = Vector3()

    def calculatePointsByCenter(self, center):
        self.center.set(center.x, center.y, center.z)
        # corners
        self.downLeft.set(center.x - self.xLengthHalf, center.y - self.yLengthHalf, center.z)
        self.downRight.set(center.x + self.xLengthHalf, center.y - self.yLengthHalf, center.z)
        self.upLeft.set(center.x - self.xLengthHalf, center.y + self.yLengthHalf, center.z)
        self.upRight.set(center.x + self.xLengthHalf, center.y + self.yLengthHalf, center.z)
        # middle
        self.middleLeft.set(center.x - self.xLengthHalf, center.y, center.z)
        self.middleRight.set(center.x + self.xLengthHalf, center.y, center.z)
        self.middleTop.set(center.x, center.y + self.yLengthHalf, center.z)
        self.middleBottom.set(center.x, center.y - self.yLengthHalf, center.z)

    def containsPoint(self, point):
        return Numeric.between(point.x, self.downLeft.x, self.downRight.x) and Numeric.between(point.y, self.downLeft.y, self.upLeft.y)

    def addZ(self, dz):
        self.center.z += dz
        self.downLeft.z += dz
        self.downRight.z += dz
        self.upLeft.z += dz
        self.upRight.z += dz
        self.middleLeft.z += dz
        self.middleRight.z += dz
        self.middleTop.z += dz
        self.middleBottom.z += dz

    def copyFrom(self, copy):
        self.center.copyFrom(copy.center)
        self.downLeft.copyFrom(copy.downLeft)
        self.downRight.copyFrom(copy.downRight)
        self.upLeft.copyFrom(copy.upLeft)
        self.upRight.copyFrom(copy.upRight)
        self.middleLeft.copyFrom(copy.middleLeft)
        self.middleRight.copyFrom(copy.middleRight)
        self.middleTop.copyFrom(copy.middleTop)
        self.middleBottom.copyFrom(copy.middleBottom)

    def __str__(self):
        return f"({self.downLeft}),({self.downRight}),({self.upLeft}),({self.upRight})"
