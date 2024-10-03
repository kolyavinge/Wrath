from game.calc.Vector3 import Vector3


class SplitPlanePosition:

    front = 1
    back = 2
    on = 3


class SplitPlane:

    def __init__(self):
        self.basePoint = Vector3()
        self.frontNormal = Vector3()
