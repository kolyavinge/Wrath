from game.calc.Vector3 import Vector3


class Rect2d:

    def __init__(self, xLength, yLength):
        self.xLength = xLength
        self.yLength = yLength
        self.xLengthHalf = xLength / 2
        self.yLengthHalf = yLength / 2
        self.downLeft = Vector3()
        self.downRight = Vector3()
        self.upLeft = Vector3()
        self.upRight = Vector3()

    def calculatePointsByCenter(self, center):
        self.downLeft.set(center.x - self.xLengthHalf, center.y - self.yLengthHalf, center.z)
        self.downRight.set(center.x + self.xLengthHalf, center.y - self.yLengthHalf, center.z)
        self.upLeft.set(center.x - self.xLengthHalf, center.y + self.yLengthHalf, center.z)
        self.upRight.set(center.x + self.xLengthHalf, center.y + self.yLengthHalf, center.z)

    def getCopy(self):
        copy = Rect2d(self.xLength, self.yLength)
        copy.downLeft = self.downLeft.getCopy()
        copy.downRight = self.downRight.getCopy()
        copy.upLeft = self.upLeft.getCopy()
        copy.upRight = self.upRight.getCopy()

        return copy
