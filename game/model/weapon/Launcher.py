from game.calc.Vector3 import Vector3
from game.model.weapon.Bullet import Bullet
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.Weapon import Weapon
from game.model.weapon.WeaponFlash import WeaponFlash


class LauncherFlash(WeaponFlash):

    def __init__(self):
        super().__init__()

    def update(self):
        pass


class LauncherBullet(Bullet):

    def __init__(self):
        super().__init__()
        self.isVisible = True
        self.velocityValue = 0.5
        self.damage = 5
        self.holeInfo = BulletHoleInfo.explosionHole


class Launcher(Weapon):

    def __init__(self):
        super().__init__(LauncherBullet, LauncherFlash)
        self.barrelPoint = Vector3(0, 0, 0.018)
        self.bulletsCount = 5
        self.maxBulletsCount = 5
        self.delay = 40
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.6
        self.feedbackLength = 0.05
        self.playerShift = Vector3(0.08, 0.1, -0.04)
