from game.calc.Vector3 import Vector3
from game.model.light.Lamp import Lamp


class Spot(Lamp):

    def __init__(self):
        super().__init__()
        self.direction = Vector3()
        self.attenuation = 0.0
        self.cutoffRadians = 0.0
