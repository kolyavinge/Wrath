from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.Weapon import Bullet, Weapon


class PistolBullet(Bullet):

    def __init__(self):
        super().__init__()
        self.velocityValue = 5
        self.damage = 5
        self.holeInfo = BulletHoleInfo.tinyHole


class Pistol(Weapon):

    def __init__(self):
        super().__init__(PistolBullet)
