from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3
from game.lib.Math import Math


class Bullet:

    def __init__(self):
        self.currentPosition = Vector3()
        self.nextPosition = Vector3()
        self.velocity = Vector3()
        self.velocityValue = 0
        self.damage = 0
        self.totalDistance = 0
        self.levelSegment = None
        self.holeInfo = None

    def commitNextPosition(self):
        self.currentPosition = self.nextPosition.copy()


class Weapon:

    def __init__(self, bulletType):
        self.bulletType = bulletType
        self.position = Vector3()
        self.direction = Vector3()
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

    def makeBullet(self):
        bullet = self.bulletType()
        bullet.currentPosition = self.position.copy()
        bullet.nextPosition = self.position.copy()
        bullet.velocity = self.direction.copy()
        bullet.velocity.setLength(bullet.velocityValue)

        return bullet

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
        modelMatrix.mul(m1)
        modelMatrix.mul(m2)
        modelMatrix.mul(m3)

        return modelMatrix
