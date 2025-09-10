from game.calc.Rect2d import Rect2d


class Box3d:

    def __init__(self, xLength, yLength, zLength):
        self.bottom = Rect2d(xLength, yLength)
        self.top = Rect2d(xLength, yLength)
        self.top.addZ(zLength)
        self.zLength = zLength

    def calculatePointsByCenter(self, center):
        self.bottom.calculatePointsByCenter(center)
        self.top.copyFrom(self.bottom)
        self.top.addZ(self.zLength)

    def copyFrom(self, copy):
        self.bottom.copyFrom(copy.bottom)
        self.top.copyFrom(copy.top)

    def __str__(self):
        return f"bottom:{self.bottom}, top:{self.top}"
