from game.calc.Vector3 import Vector3
from game.model.Visible import Visible


class Light(Visible):

    def __init__(self):
        super().__init__()
        self.color = Vector3(1.0, 1.0, 1.0)
