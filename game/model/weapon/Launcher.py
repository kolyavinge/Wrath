from game.calc.Geometry import Geometry
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
        self.velocityValue = 1.0
        self.damagePercent = 0.5
        self.holeInfo = BulletHoleInfo.explosionHole

    def update(self):
        self.rollRadians = Geometry.normalizeRadians(self.rollRadians + 0.25)


class Launcher(Weapon):

    def __init__(self):
        super().__init__(LauncherBullet, LauncherFlash)
        self.barrelPoint = Vector3(0, 0, 0.05)
        self.bulletsCount = 5
        self.maxBulletsCount = 5
        self.delay = 40
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.6
        self.feedbackLength = 0.05
        self.playerShift = Vector3(0.15, 0.1, -0.06)
        self.enemyShift = Vector3(0.2, 0.2, -0.04)
