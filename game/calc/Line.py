from game.calc.Vector3 import Vector3


class Line:

    def __init__(self):
        self.startPoint = Vector3()
        self.endPoint = Vector3()

    def __str__(self):
        return f"{self.startPoint} - {self.endPoint}"
