from game.calc.Geometry import Geometry
from game.model.light.Torch import Torch


class PlayerItems:

    def __init__(self):
        self.torch = Torch()
        self.torch.attenuation = 25.0
        self.torch.cutoffRadians = Geometry.degreesToRadians(5.0)
