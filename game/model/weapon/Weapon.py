from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.weapon import Bullet


class Weapon:

    def __init__(self):
        self.position = Vector3()
        self.direction = Vector3()
        self.yawRadians = 0
        self.pitchRadians = 0
        self.bulletsCount = 0
        self.maxBulletsCount = 0
        self.bulletSpeed = 0
        self.bulletDamage = 0

    def makeBullet(self):
        bullet = Bullet()
        bullet.prevPosition = self.position
        bullet.position = self.position
        bullet.direction = self.direction
        bullet.speed = self.bulletSpeed
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
