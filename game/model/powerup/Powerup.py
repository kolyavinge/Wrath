from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3


class Powerup:

    def __init__(self):
        self.position = Vector3()
        self.pickupPosition = Vector3()
        self.height = 0
        self.rotateRadians = 0
        self.collisionLevelSegment = None
        self.visibilityLevelSegment = None

    def setPosition(self, position):
        self.pickupPosition = position
        self.position = position.copy()
        self.position.z += self.height

    def update(self):
        pass

    def getModelMatrix(self):
        m1 = TransformMatrix4()
        m1.translate(self.position.x, self.position.y, self.position.z)

        m2 = TransformMatrix4()
        m2.rotate(self.rotateRadians, CommonConstants.zAxis)

        modelMatrix = TransformMatrix4()
        modelMatrix.setIdentity()
        modelMatrix.mul(m1)
        modelMatrix.mul(m2)

        return modelMatrix
