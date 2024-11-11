from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.light.Spot import Spot


class Torch(Spot):

    def __init__(self):
        super().__init__()
        self.isActive = False
        self.color = Vector3(1.0, 1.0, 1.0)
        self.color.mul(5.0)
        self.attenuation = 200.0
        self.cutoffCos = Math.cos(Geometry.degreesToRadians(30.0))

    def switch(self):
        self.isActive = not self.isActive
