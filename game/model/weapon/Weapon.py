from game.calc.Vector3 import Vector3


class Weapon:

    def __init__(self):
        self.bulletsCount = 0
        self.maxBulletsCount = 0
        self.damage = 0
        self.speed = 0
        self.direction = Vector3()
