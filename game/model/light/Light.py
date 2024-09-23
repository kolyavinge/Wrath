from game.calc.Vector3 import Vector3
from game.model.Material import Material


class Light:

    def __init__(self):
        self.color = Vector3(1.0, 1.0, 1.0)
        self.material = Material.blank
