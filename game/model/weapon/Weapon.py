from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.calc.Vector3 import Vector3
from game.lib.Math import Math


class Flash:

    def __init__(self):
        self.weaponType = None
        self.alpha = 0
        self.isVisible = True

    def update(self):
        pass

    def calculateModelMatrix(self, position, yawRadians, pitchRadians):
        self.modelMatrix = (
            TransformMatrix4Builder()
            .translate(position.x, position.y, position.z)
            .rotate(yawRadians, CommonConstants.zAxis)
            .rotate(pitchRadians, CommonConstants.xAxis)
            .resultMatrix
        )

    def getModelMatrix(self):
        return self.modelMatrix


class Bullet:

    def __init__(self):
        self.isVisible = False
        self.currentPosition = Vector3()
        self.nextPosition = Vector3()
        self.velocity = Vector3()
        self.velocityValue = 0
        self.damage = 0
        self.totalDistance = 0
        self.currentLevelSegment = None
        self.nextLevelSegment = None
        self.currentVisibilityLevelSegment = None
        self.holeInfo = None

    def commitNextPosition(self):
        self.currentPosition = self.nextPosition.copy()


class Weapon:

    defaultCount = 1

    def __init__(self, bulletType, flashType):
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

    def makeBullet(self):
        bullet = self.bulletType()
        bullet.currentPosition = self.barrelPosition.copy()
        bullet.nextPosition = bullet.currentPosition.copy()
        bullet.velocity = self.direction.copy()
        bullet.velocity.setLength(bullet.velocityValue)

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
