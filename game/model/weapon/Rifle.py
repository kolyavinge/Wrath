from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.Weapon import Bullet, Weapon


class RifleBullet(Bullet):

    def __init__(self):
        super().__init__()
        self.velocityValue = 5
        self.damage = 5
        self.holeInfo = BulletHoleInfo.tinyHole


class Rifle(Weapon):

    def __init__(self):
        super().__init__(RifleBullet)
        self.bulletsCount = 2000
        self.maxBulletsCount = 2000
        self.delay = 10
