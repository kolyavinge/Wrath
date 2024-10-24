from game.calc.Vector3 import Vector3
from game.model.Visible import Visible


class BulletHole(Visible):

    def __init__(self, bulletHoleInfo):
        super().__init__()
        self.material = bulletHoleInfo.material
        self.halfSize = bulletHoleInfo.halfSize
        self.frontNormal = Vector3()
        self.point1 = Vector3()
        self.point2 = Vector3()
        self.point3 = Vector3()
        self.point4 = Vector3()
        self.levelSegment = None
