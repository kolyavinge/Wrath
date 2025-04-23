from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.calc.Vector3 import Vector3
from game.lib.Math import Math


class Weapon:

    defaultCount = 1

    def __init__(self, bulletType, flashType=None):
        self.bulletType = bulletType
        self.flashType = flashType
        self.position = Vector3()
        self.direction = Vector3()
        self.barrelPoint = Vector3()
        self.barrelPosition = Vector3()
        self.yawRadians = 0
        self.pitchRadians = 0
        self.bulletsCount = 0
        self.maxBulletsCount = 0
        self.delay = 0
        self.delayRemain = 0
        self.jitter = Vector3()
        self.jitterFade = 0
        self.jitterDelta = 0
        self.feedback = Vector3()
        self.feedbackFade = 0
        self.feedbackLength = 0
        self.playerShift = Vector3()
        self.enemyShift = Vector3()

    def makeBullet(self, ownerPerson):
        bullet = self.bulletType()
        bullet.currentPosition = self.barrelPosition.copy()
        bullet.nextPosition = bullet.currentPosition.copy()
        bullet.yawRadians = self.yawRadians
        bullet.pitchRadians = self.pitchRadians
        bullet.velocity = self.direction.copy()
        bullet.velocity.setLength(bullet.velocityValue)
        bullet.ownerPerson = ownerPerson

        return bullet

    def makeFlash(self):
        if self.flashType is None:
            return None

        flash = self.flashType()
        flash.weaponType = type(self)
        flash.calculateModelMatrix(self.barrelPosition, self.yawRadians, self.pitchRadians)

        return flash

    def addBullets(self, count):
        self.bulletsCount = Math.min(self.bulletsCount + count, self.maxBulletsCount)

    def getModelMatrix(self):
        return (
            TransformMatrix4Builder()
            .translate(self.position.x, self.position.y, self.position.z)
            .rotate(self.yawRadians, CommonConstants.zAxis)
            .rotate(self.pitchRadians, CommonConstants.xAxis)
            .resultMatrix
        )

    @staticmethod
    def getAllWeaponTypes():
        return Weapon.__subclasses__()
