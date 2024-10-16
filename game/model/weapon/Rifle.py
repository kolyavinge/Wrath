from game.model.weapon.Weapon import Weapon


class Rifle(Weapon):

    def __init__(self):
        super().__init__()
        self.maxBulletsCount = 200
        self.bulletSpeed = 5
        self.bulletDamage = 5
