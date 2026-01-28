from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4 import TransformMatrix4
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.lib.Random import Random
from game.model.powerup.PowerupKind import PowerupKind


class Powerup:

    def __init__(self):
        self.id = 0
        self.kind = PowerupKind.unknown
        self.position = Vector3()
        self.pickupPosition = Vector3()
        self.height = 0
        self.rotateRadians = 0
        self.collisionLevelSegment = None
        self.visibilityLevelSegment = None
        self.canCastShadow = False

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

    def setRandomRotate(self):
        self.rotateRadians = Random.getFloat(0, Math.piDouble)
