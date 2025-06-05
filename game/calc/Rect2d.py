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
        self.center = center.copy()
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

    def copy(self):
        copy = Rect2d(self.xLength, self.yLength)
        copy.center = self.center.copy()
        copy.downLeft = self.downLeft.copy()
        copy.downRight = self.downRight.copy()
        copy.upLeft = self.upLeft.copy()
        copy.upRight = self.upRight.copy()
        copy.middleLeft = self.middleLeft.copy()
        copy.middleRight = self.middleRight.copy()
        copy.middleTop = self.middleTop.copy()
        copy.middleBottom = self.middleBottom.copy()

        return copy

    def __str__(self):
        return f"({self.downLeft}),({self.downRight}),({self.upLeft}),({self.upRight})"
