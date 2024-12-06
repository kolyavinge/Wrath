class SplitPlanePosition:

    front = 1
    back = 2
    on = 3


class SplitPlane:

    def __init__(self, basePoint=None, frontNormal=None):
        self.basePoint = basePoint
        self.frontNormal = frontNormal
