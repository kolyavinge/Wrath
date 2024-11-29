from game.lib.Numeric import Numeric


class Plane:

    def __init__(self, normal, point):
        if normal.isZero():
            raise Exception("Normal vector cannot be zero.")

        self.a = normal.x
        self.b = normal.y
        self.c = normal.z
        self.d = -normal.dotProduct(point)

    def containsPoint(self, point, eps=0.0001):
        v = self.a * point.x + self.b * point.y + self.c * point.z + self.d
        return Numeric.floatEquals(v, 0, eps)

    def getX(self, y, z):
        if self.a == 0:
            return None
        return -(self.b * y + self.c * z + self.d) / self.a

    def getY(self, x, z):
        if self.b == 0:
            return None
        return -(self.a * x + self.c * z + self.d) / self.b

    def getZ(self, x, y):
        if self.c == 0:
            return None
        return -(self.a * x + self.b * y + self.d) / self.c

    @staticmethod
    def makeByThreePoints(p0, p1, p2):
        v1 = p1.copy()
        v1.sub(p0)
        v2 = p2.copy()
        v2.sub(p0)
        v1.vectorProduct(v2)
        v1.normalize()

        return Plane(v1, p0)
