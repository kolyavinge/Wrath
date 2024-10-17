from game.model.weapon.Weapon import Weapon


class Rifle(Weapon):

    def __init__(self):
        super().__init__()
        self.bulletsCount = 2000
        self.maxBulletsCount = 2000
        self.bulletVelocity = 5
        self.bulletDamage = 5
        self.delay = 10
