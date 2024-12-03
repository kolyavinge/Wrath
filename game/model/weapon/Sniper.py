from game.calc.Vector3 import Vector3
from game.model.weapon.Bullet import Bullet
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.SimpleFlash import SimpleFlash
from game.model.weapon.Weapon import Weapon


class SniperFlash(SimpleFlash):

    def __init__(self):
        super().__init__()


class SniperBullet(Bullet):

    def __init__(self):
        super().__init__()
        self.velocityValue = 5
        self.damagePercent = 1.0
        self.holeInfo = BulletHoleInfo.largeHole


class Sniper(Weapon):

    def __init__(self):
        super().__init__(SniperBullet, SniperFlash)
        self.barrelPoint = Vector3(0, 0.3, 0.03)
        self.bulletsCount = 8
        self.maxBulletsCount = 8
        self.delay = 80
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.9
        self.feedbackLength = 0.3
        self.playerShift = Vector3(0.1, 0.25, -0.08)
