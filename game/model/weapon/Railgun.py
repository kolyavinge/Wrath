from game.anx.PersonConstants import PersonConstants
from game.calc.Vector3 import Vector3
from game.lib.DecrementCounter import DecrementCounter
from game.model.Material import Material
from game.model.weapon.Bullet import Bullet
from game.model.weapon.BulletHoleInfo import BulletHoleInfo
from game.model.weapon.BulletTrace import RayBulletTrace
from game.model.weapon.Weapon import Weapon


class RailgunBulletTrace(RayBulletTrace):

    def __init__(self):
        super().__init__()
        self.fade = 0.01
        self.material = Material.railgunBulletTrace


class RailgunBullet(Bullet):
    def __init__(self):
        super().__init__(RailgunBulletTrace)
        self.velocityValue = 6
        self.chargedVelocityFactor = 10
        self.damagePercent = 0.8
        self.goThroughPerson = True
        self.damagedPersonSet = set()
        self.paralyze = True
        self.paralyzeTime = 100
        self.isCharged = False
        self.holeInfo = BulletHoleInfo.railgunHole


class Railgun(Weapon):

    def __init__(self):
        super().__init__(RailgunBullet)
        self.barrelPoint = Vector3(0.003, -0.02, 0.01)
        self.bulletsCount = 10
        self.maxBulletsCount = 10
        self.delay = 20
        self.jitterFade = 0.9
        self.jitterDelta = 0.05
        self.feedbackFade = 0.6
        self.feedbackLength = 0.05
        self.playerShift = Vector3(0.1, 0.3, -0.11)
        self.enemyShift = Vector3(0.16, 0.5, -0.1)
        self.selectionShift = Vector3(0, -0.25, 0)
        self.cannotBeChangedWhileAltFire = True
        self.chargeDelay = DecrementCounter(40)
        self.altFireLimitDelay = DecrementCounter(100)
        self.isCharged = False

    def makeBullet(self, ownerPerson):
        bullet = super().makeBullet(ownerPerson)

        if self.isCharged:
            bullet.velocityValue *= bullet.chargedVelocityFactor
            bullet.velocity.mul(bullet.chargedVelocityFactor)
            bullet.damagePercent = PersonConstants.maxDamagePercent
            bullet.isCharged = True
            self.isCharged = False

        return bullet

    @staticmethod
    def getChargingDisplayPosition(displayIndex):
        downLeft = Vector3(-0.0043, -0.11805, 0.0857)
        width = 0.0114
        height = 0.0025
        heightStep = 0.003

        return (
            Vector3(downLeft.x, downLeft.y, downLeft.z + displayIndex * heightStep),
            Vector3(downLeft.x + width, downLeft.y, downLeft.z + displayIndex * heightStep),
            Vector3(downLeft.x + width, downLeft.y, downLeft.z + height + displayIndex * heightStep),
            Vector3(downLeft.x, downLeft.y, downLeft.z + height + displayIndex * heightStep),
        )
