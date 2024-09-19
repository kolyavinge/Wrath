from game.calc.Vector3 import Vector3


class Light:

    def __init__(self):
        self.position = Vector3()
        self.color = Vector3(1.0, 1.0, 1.0)
