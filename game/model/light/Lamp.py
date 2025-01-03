from game.calc.Vector3 import Vector3
from game.model.light.Light import Light
from game.model.Visible import Visible


class Lamp(Light, Visible):

    def __init__(self):
        Light.__init__(self)
        Visible.__init__(self)
        self.frontNormal = Vector3()

    def commit(self):
        self.lightPosition = self.frontNormal.copy()
        self.lightPosition.setLength(0.1)
        self.lightPosition.add(self.position)
