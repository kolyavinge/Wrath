from game.calc.Vector3 import Vector3


class Bullet:

    def __init__(self):
        self.prevPosition = Vector3()
        self.position = Vector3()
        self.direction = Vector3()
        self.speed = 0
        self.damage = 0
