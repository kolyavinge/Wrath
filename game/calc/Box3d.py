from game.calc.Rect2d import Rect2d


class Box3d:

    def __init__(self, xLength, yLength, zLength):
        self.bottom = Rect2d(xLength, yLength)
        self.top = Rect2d(xLength, yLength)
        self.zLength = zLength

    def calculatePointsByCenter(self, center):
        self.bottom.calculatePointsByCenter(center)
        self.top = self.bottom.copy()
        self.top.downLeft.z += self.zLength
        self.top.downRight.z += self.zLength
        self.top.upLeft.z += self.zLength
        self.top.upRight.z += self.zLength
        self.top.middleLeft.z += self.zLength
        self.top.middleRight.z += self.zLength
        self.top.middleTop.z += self.zLength
        self.top.middleBottom.z += self.zLength

    def copy(self):
        copy = Box3d(self.bottom.xLength, self.bottom.yLength, self.zLength)
        copy.bottom = self.bottom.copy()
        copy.top = self.top.copy()
        copy.zLength = self.zLength

        return copy

    def __str__(self):
        return f"bottom:{self.bottom}, top:{self.top}"
