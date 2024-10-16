from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3
from game.lib.Math import Math


class Bullet:

    def __init__(self):
        self.prevPosition = Vector3()
        self.position = Vector3()
        self.velocity = Vector3()
        self.velocityValue = 0
        self.damage = 0
        self.totalDistance = 0


class Weapon:

    def __init__(self):
        self.position = Vector3()
        self.direction = Vector3()
        self.yawRadians = 0
        self.pitchRadians = 0
        self.bulletsCount = 0
        self.maxBulletsCount = 0
        self.bulletVelocity = 0
        self.bulletDamage = 0
        self.isFiring = False

    def makeBullet(self):
        bullet = Bullet()
        bullet.prevPosition = self.position.copy()
        bullet.position = self.position.copy()
        bullet.velocityValue = self.bulletVelocity
        bullet.velocity = self.direction.copy()
        bullet.velocity.setLength(self.bulletVelocity)
        bullet.damage = self.bulletDamage

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
