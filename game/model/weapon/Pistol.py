from game.calc.Vector3 import Vector3
from game.model.Material import Material
from game.model.weapon.Bullet import Bullet
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.BulletTrace import BulletTrace
from game.model.weapon.SimpleFlash import SimpleFlash
from game.model.weapon.Weapon import Weapon


class PistolFlash(SimpleFlash):

    def __init__(self):
        super().__init__()


class PistolBulletTrace(BulletTrace):

    def __init__(self):
        super().__init__()
        self.fade = 0.1
        self.material = Material.commonBulletTrace


class PistolBullet(Bullet):

    def __init__(self):
        super().__init__(PistolBulletTrace)
        self.velocityValue = 4
        self.damagePercent = 0.1
        self.holeInfo = BulletHoleInfo.smallHole


class Pistol(Weapon):

    defaultCount = 2

    def __init__(self):
        super().__init__(PistolBullet, PistolFlash)
        self.barrelPoint = Vector3(0, 0.14, 0.02)
        self.isBurstModeEnabled = True
        self.minBurstCount = 2
        self.maxBurstCount = 8
        self.bulletsCount = 25
        self.maxBulletsCount = 25
        self.delay = 10
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.6
        self.feedbackLength = 0.05
        self.playerShift = Vector3(0.15, 0.3, -0.1)
        self.enemyShift = Vector3(0.18, 0.5, -0.1)
        self.selectionShift = Vector3(0, -0.15, 0)
