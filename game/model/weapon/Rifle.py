from game.calc.Vector3 import Vector3
from game.model.Material import Material
from game.model.weapon.Bullet import Bullet
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.BulletTrace import BulletTrace
from game.model.weapon.SimpleFlash import SimpleFlash
from game.model.weapon.Weapon import Weapon


class RifleFlash(SimpleFlash):

    def __init__(self):
        super().__init__()


class RifleBulletTrace(BulletTrace):

    def __init__(self):
        super().__init__()
        self.fade = 0.1
        self.material = Material.commonBulletTrace


class RifleBullet(Bullet):

    def __init__(self):
        super().__init__(RifleBulletTrace)
        self.velocityValue = 5
        self.damagePercent = 0.2
        self.holeInfo = BulletHoleInfo.smallHole


class Rifle(Weapon):

    def __init__(self):
        super().__init__(RifleBullet, RifleFlash)
        self.barrelPoint = Vector3(0, 0.4, 0.04)
        self.bulletsCount = 50
        self.maxBulletsCount = 50
        self.delay = 8
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.6
        self.feedbackLength = 0.05
        self.playerShift = Vector3(0.1, 0.2, -0.11)
        self.enemyShift = Vector3(0.15, 0.3, -0.1)
