from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3


class Powerup:

    def __init__(self):
        self.position = Vector3()
        self.height = 0
        self.rotateRadians = 0

    def update(self):
        pass

    def getModelMatrix(self, scale=1.0):
        m1 = TransformMatrix4()
        m1.translate(self.position.x, self.position.y, self.position.z)

        m2 = TransformMatrix4()
        m2.rotate(self.rotateRadians, CommonConstants.zAxis)

        m3 = TransformMatrix4()
        m3.scale(scale, scale, scale)

        modelMatrix = TransformMatrix4()
        modelMatrix.mul(m1)
        modelMatrix.mul(m2)
        modelMatrix.mul(m3)

        return modelMatrix
