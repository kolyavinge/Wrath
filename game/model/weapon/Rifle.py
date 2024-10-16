from game.model.weapon.Weapon import Weapon


class Rifle(Weapon):

    def __init__(self):
        super().__init__()
        self.bulletsCount = 200
        self.maxBulletsCount = 200
        self.bulletVelocity = 5
        self.bulletDamage = 5
