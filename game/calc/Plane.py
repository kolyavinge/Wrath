class Plane:

    def __init__(self, normal, point):
        self.a = normal.x
        self.b = normal.y
        self.c = normal.z
        self.d = -normal.dotProduct(point)
