from game.calc.Vector3 import Vector3
from game.model.light.Light import Light


class Lamp(Light):

    def __init__(self):
        super().__init__()
        self.position = Vector3()
        self.frontNormal = Vector3()

    def commit(self):
        self.lightPosition = self.frontNormal.copy()
        self.lightPosition.setLength(0.1)
        self.lightPosition.add(self.position)
