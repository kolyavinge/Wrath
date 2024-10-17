from game.lib.Numeric import Numeric


class Plane:

    def __init__(self, normal, point):
        self.a = normal.x
        self.b = normal.y
        self.c = normal.z
        self.d = -normal.dotProduct(point)

    def containsPoint(self, point, eps=0.0001):
        v = self.a * point.x + self.b * point.y + self.c * point.z + self.d
        return Numeric.floatEquals(v, 0, eps)

    def getZ(self, x, y):
        assert self.c != 0
        z = -(self.a * x + self.b * y + self.d) / self.c

        return z
