from game.calc.Geometry import Geometry
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.light.Torch import Torch
from game.model.weapon.Rifle import Rifle


class PlayerItems:

    def __init__(self):
        self.torch = Torch()
        self.torch.color = Vector3(1.0, 1.0, 1.0)
        self.torch.color.mul(5.0)
        self.torch.attenuation = 200.0
        self.torch.cutoffCos = Math.cos(Geometry.degreesToRadians(30.0))
        self.torch.switch()
        self.currentWeapon = Rifle()
