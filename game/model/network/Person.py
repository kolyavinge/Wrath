from game.calc.Vector3 import Vector3


class Person:

    def __init__(self):
        self.id = 0
        self.centerPoint = Vector3()
        self.lookDirection = Vector3()

    def __eq__(self, value):
        return self.centerPoint == value.centerPoint and self.lookDirection == value.lookDirection

    def __hash__(self):
        return hash((self.centerPoint.__hash__(), self.lookDirection.__hash__()))
