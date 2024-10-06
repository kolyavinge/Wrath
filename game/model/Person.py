from game.calc.Vector3 import Vector3
from game.model.level.Floor import Floor


class Person:

    def __init__(self):
        self.currentCenterPoint = Vector3()
        self.currentFloor = Floor()
