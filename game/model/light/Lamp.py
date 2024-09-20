from game.calc.Vector3 import Vector3
from game.model.light.LightSource import LightSource


class Lamp(LightSource):

    def __init__(self):
        super().__init__()
        self.position = Vector3()
