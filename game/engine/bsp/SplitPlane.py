from game.calc.Vector3 import Vector3


class SplitPlane:

    def __init__(self):
        self.priority = 0  # remove
        self.basePoint = Vector3()
        self.frontNormal = Vector3()
