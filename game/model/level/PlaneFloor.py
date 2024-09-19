from game.calc.Plane import Plane
from game.calc.Vector3 import Vector3
from game.model.level.Floor import Floor


class PlaneFloor(Floor):

    def __init__(self):
        super().__init__()

    def commit(self):
        self.plane = Plane(self.upNormal, self.downLeft)

    def getZ(self, x, y):
        return self.plane.getZ(x, y)
