from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.Weapon import Bullet, Weapon


class LauncherBullet(Bullet):

    def __init__(self):
        super().__init__()
        self.velocityValue = 5
        self.damage = 5
        self.holeInfo = BulletHoleInfo.tinyHole


class Launcher(Weapon):

    def __init__(self):
        super().__init__(LauncherBullet)
