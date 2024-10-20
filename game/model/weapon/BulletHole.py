from game.calc.Vector3 import Vector3
from game.model.Material import Material
from game.model.Visible import Visible


class BulletHole(Visible):

    halfSize = 0.05

    def __init__(self):
        super().__init__()
        self.material = Material.bulletHole
        self.point1 = Vector3()
        self.point2 = Vector3()
        self.point3 = Vector3()
        self.point4 = Vector3()
