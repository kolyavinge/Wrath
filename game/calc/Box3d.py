from game.calc.Rect2d import Rect2d


class Box3d:

    def __init__(self, xLength, yLength, zLength):
        self.bottom = Rect2d(xLength, yLength)
        self.top = Rect2d(xLength, yLength)
        self.zLength = zLength

    def calculatePointsByCenter(self, center):
        self.bottom.calculatePointsByCenter(center)
        self.top = self.bottom.getCopy()
        self.top.downLeft.z += self.zLength
        self.top.downRight.z += self.zLength
        self.top.upLeft.z += self.zLength
        self.top.upRight.z += self.zLength

    def getCopy(self):
        copy = Box3d(self.bottom.xLength, self.bottom.yLength, self.zLength)
        copy.bottom = self.bottom.getCopy()
        copy.top = self.top.getCopy()
        copy.zLength = self.zLength

        return copy
