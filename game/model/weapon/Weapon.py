from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4 import TransformMatrix4
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
        m1 = TransformMatrix4()
        m1.translate(position.x, position.y, position.z)

        m2 = TransformMatrix4()
        m2.rotate(yawRadians, CommonConstants.zAxis)

        m3 = TransformMatrix4()
        m3.rotate(pitchRadians, CommonConstants.xAxis)

        self.modelMatrix = TransformMatrix4()
        self.modelMatrix.setIdentity()
        self.modelMatrix.mul(m1)
        self.modelMatrix.mul(m2)
        self.modelMatrix.mul(m3)

    def getModelMatrix(self):
        return self.modelMatrix


class Bullet:

    def __init__(self):
        self.currentPosition = Vector3()
        self.nextPosition = Vector3()
        self.velocity = Vector3()
        self.velocityValue = 0
        self.damage = 0
        self.totalDistance = 0
        self.currentLevelSegment = None
        self.nextLevelSegment = None
        self.holeInfo = None

    def commitNextPosition(self):
        self.currentPosition = self.nextPosition.copy()


class Weapon:

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
        self.isFiring = False
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
        flash = self.flashType()
        flash.weaponType = type(self)
        flash.calculateModelMatrix(self.barrelPosition, self.yawRadians, self.pitchRadians)

        return flash

    def addBullets(self, count):
        self.bulletsCount = Math.min(self.bulletsCount + count, self.maxBulletsCount)

    def getModelMatrix(self):
        m1 = TransformMatrix4()
        m1.translate(self.position.x, self.position.y, self.position.z)

        m2 = TransformMatrix4()
        m2.rotate(self.yawRadians, CommonConstants.zAxis)

        m3 = TransformMatrix4()
        m3.rotate(self.pitchRadians, CommonConstants.xAxis)

        modelMatrix = TransformMatrix4()
        modelMatrix.setIdentity()
        modelMatrix.mul(m1)
        modelMatrix.mul(m2)
        modelMatrix.mul(m3)

        return modelMatrix

    @staticmethod
    def getAllWeaponTypes():
        return Weapon.__subclasses__()
