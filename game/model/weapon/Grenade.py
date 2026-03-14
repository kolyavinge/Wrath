from game.anx.CommonConstants import CommonConstants
from game.calc.Geometry import Geometry
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.calc.Vector3 import Vector3
from game.lib.DecrementCounter import DecrementCounter


class Grenade:

    def __init__(self, explosionType):
        self.id = 0
        self.explosionType = explosionType
        self.startPosition = Vector3()
        self.currentPosition = Vector3()
        self.nextPosition = Vector3()
        self.pitchRadians = 0
        self.yawRadians = 0
        self.direction = Vector3()
        self.velocity = Vector3()
        self.velocityValue = 0
        self.damagePercent = 0
        self.detonationTimeout = DecrementCounter()
        self.currentLevelSegment = None
        self.nextLevelSegment = None
        self.currentVisibilityLevelSegment = None
        self.holeInfo = None
        self.weapon = None
        self.ownerPerson = None
        self.randomSeed = None

    def update(self):
        self.pitchRadians = Geometry.normalizeRadians(self.pitchRadians + 0.1)
        self.yawRadians = Geometry.normalizeRadians(self.yawRadians + 0.1)

    def makeExplosion(self):
        explosion = self.explosionType()
        explosion.bullet = self
        explosion.position = self.currentPosition.copy()

        return explosion

    def getModelMatrix(self):
        return (
            TransformMatrix4Builder()
            .translate(self.currentPosition.x, self.currentPosition.y, self.currentPosition.z)
            .rotate(self.yawRadians, CommonConstants.zAxis)
            .rotate(self.pitchRadians, CommonConstants.xAxis)
            .resultMatrix
        )
