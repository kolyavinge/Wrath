from game.calc.Vector3 import Vector3


class FlatFloor:

    def __init__(self):
        self.downLeft = Vector3()
        self.downRight = Vector3()
        self.upLeft = Vector3()
        self.upRight = Vector3()
        self.leftFrontNormal = Vector3()
        self.rightFrontNormal = Vector3()
        self.upFrontNormal = Vector3()
        self.downFrontNormal = Vector3()
        self.z = 0

    def getZ(self, x, y):
        return self.z

    def __str__(self):
        return f"({self.downLeft}),({self.downRight}),({self.upLeft}),({self.upRight})"
