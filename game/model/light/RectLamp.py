from game.calc.Vector3 import Vector3
from game.model.light.Lamp import Lamp


class RectLamp(Lamp):

    def __init__(self):
        super().__init__()
        self.height = 0
        self.width = 0
        self.long = 0
        self.longNormal = Vector3()
