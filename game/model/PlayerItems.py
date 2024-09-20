from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.light.Torch import Torch


class PlayerItems:

    def __init__(self):
        self.torch = Torch()
        self.torch.color = Vector3(4.0, 4.0, 4.0)
        self.torch.attenuation = 150.0
        self.torch.cutoffCos = Math.cos(Geometry.degreesToRadians(25.0))
