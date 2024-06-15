from game.calc.Vector3 import Vector3


class Rect2d:

    def __init__(self):
        self.downLeft = Vector3()
        self.downRight = Vector3()
        self.upLeft = Vector3()
        self.upRight = Vector3()
