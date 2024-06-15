from game.calc.Vector3 import Vector3


class Rect2d:

    def __init__(self):
        self.downLeft = Vector3()
        self.downRight = Vector3()
        self.upLeft = Vector3()
        self.upRight = Vector3()

    def moveByVector(self, vector):
        self.downLeft.add(vector)
        self.downRight.add(vector)
        self.upLeft.add(vector)
        self.upRight.add(vector)

    def getCopy(self):
        copy = Rect2d()
        copy.downLeft = self.downLeft.getCopy()
        copy.downRight = self.downRight.getCopy()
        copy.upLeft = self.upLeft.getCopy()
        copy.upRight = self.upRight.getCopy()

        return copy
