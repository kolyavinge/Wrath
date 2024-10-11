from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3


class Weapon:

    def __init__(self):
        self.bulletsCount = 0
        self.maxBulletsCount = 0
        self.damage = 0
        self.speed = 0
        self.direction = Vector3()

    def getModelMatrix(self, player):
        m1 = TransformMatrix4()
        m1.translate(player.eyePosition.x, player.eyePosition.y, player.eyePosition.z - 0.2)

        m2 = TransformMatrix4()
        m2.rotate(player.yawRadians, CommonConstants.zAxis)

        m3 = TransformMatrix4()
        m3.rotate(player.pitchRadians, CommonConstants.xAxis)

        modelMatrix = TransformMatrix4()
        modelMatrix.mul(m1)
        modelMatrix.mul(m2)
        modelMatrix.mul(m3)

        return modelMatrix
