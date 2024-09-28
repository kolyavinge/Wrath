from game.calc.Vector3 import Vector3


class Matrix3:

    def __init__(self, items):
        self.items = items

    def mulVector3(self, v):
        x = self.items[0] * v.x + self.items[3] * v.y + self.items[6] * v.z
        y = self.items[1] * v.x + self.items[4] * v.y + self.items[7] * v.z
        z = self.items[2] * v.x + self.items[5] * v.y + self.items[8] * v.z

        return Vector3(x, y, z)
