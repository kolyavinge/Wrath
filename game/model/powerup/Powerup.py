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
        modelMatrix = TransformMatrix4()
        modelMatrix.translateAndRotate(self.position.x, self.position.y, self.position.z, self.rotateRadians, CommonConstants.zAxis)

        return modelMatrix
