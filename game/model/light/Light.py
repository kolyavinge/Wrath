from game.calc.Vector3 import Vector3


class Light:

    def __init__(self):
        self.color = Vector3(1.0, 1.0, 1.0)
        self.lightPosition = Vector3()
        self.joinGroup = None

    def commit(self):
        pass
