from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.Weapon import Bullet, Flash, Weapon


class PistolFlash(Flash):

    def __init__(self):
        super().__init__()

    def update(self):
        pass


class PistolBullet(Bullet):

    def __init__(self):
        super().__init__()
        self.barrelLength = 0.2
        self.velocityValue = 5
        self.damage = 5
        self.holeInfo = BulletHoleInfo.tinyHole


class Pistol(Weapon):

    def __init__(self):
        super().__init__(PistolBullet, PistolFlash)
