class Plane:

    def __init__(self, normal, point):
        self.a = normal.x
        self.b = normal.y
        self.c = normal.z
        self.d = -normal.dotProduct(point)

    def getZ(self, x, y):
        assert self.c != 0
        z = -(self.a * x + self.b * y + self.d) / self.c

        return z
