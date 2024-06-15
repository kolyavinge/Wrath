from game.calc.Rect2d import Rect2d


class Rect3d:

    def __init__(self):
        self.bottom = Rect2d()
        self.top = Rect2d()
        self.height = 1

    def moveByVector(self, vector):
        self.bottom.moveByVector(vector)
        self.top.moveByVector(vector)

    def getCopy(self):
        copy = Rect3d()
        copy.bottom = self.bottom.getCopy()
        copy.top = self.top.getCopy()
        copy.height = self.height

        return copy
