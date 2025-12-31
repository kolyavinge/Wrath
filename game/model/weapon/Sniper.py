from game.calc.Vector3 import Vector3
from game.lib.DecrementCounter import DecrementCounter
from game.model.Material import Material
from game.model.weapon.Bullet import Bullet
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.BulletTrace import RayBulletTrace
from game.model.weapon.SimpleFlash import SimpleFlash
from game.model.weapon.Weapon import Weapon


class SniperFlash(SimpleFlash):

    def __init__(self):
        super().__init__()


class SniperBulletTrace(RayBulletTrace):

    def __init__(self):
        super().__init__()
        self.fade = 0.05
        self.material = Material.commonBulletTrace


class SniperBullet(Bullet):

    def __init__(self):
        super().__init__(SniperBulletTrace)
        self.velocityValue = 10.0
        self.damagePercent = 0.9
        self.isHeadshotEnabled = True
        self.holeInfo = BulletHoleInfo.largeHole


class Sniper(Weapon):

    def __init__(self):
        super().__init__(SniperBullet, SniperFlash)
        self.bulletsCount = 8
        self.maxBulletsCount = 8
        self.delay = 70
        self.needReload = True
        self.allowFireWithAltFire = True
        self.reloadDelay = 15
        self.reloadDelayRemain = DecrementCounter()
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.9
        self.feedbackLength = 0.3
        self.slowdownCoeff = 0.85
        self.setPositionForDefaultAimState()

    def setPositionForDefaultAimState(self):
        self.barrelPoint = Vector3(0, 0.6, 0.04)
        self.playerShift = Vector3(0.12, 0.4, -0.12)
        self.enemyShift = Vector3(0.18, 0.4, -0.08)
        self.selectionShift = Vector3(0, -0.35, 0)

    def setPositionForSniperAimState(self):
        self.barrelPoint = Vector3(0, 0, 0.027)
        self.playerShift = Vector3(0.0025, 0.25, -0.06)
