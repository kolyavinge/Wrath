from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.calc.Vector3 import Vector3


class Bullet:

    def __init__(self, traceType=None, explosionType=None):
        self.traceType = traceType
        self.explosionType = explosionType
        self.isVisible = False
        self.currentPosition = Vector3()
        self.nextPosition = Vector3()
        self.pitchRadians = 0
        self.rollRadians = 0
        self.yawRadians = 0
        self.velocity = Vector3()
        self.velocityValue = 0
        self.damagePercent = 0
        self.totalDistance = 0
        self.currentLevelSegment = None
        self.nextLevelSegment = None
        self.currentVisibilityLevelSegment = None
        self.goThroughPerson = False
        self.isHeadshotEnabled = False
        self.holeInfo = None
        self.ownerPerson = None

    def commitNextPosition(self):
        self.currentPosition = self.nextPosition.copy()

    def update(self):
        pass

    def makeTrace(self):
        if self.traceType is None:
            return None

        trace = self.traceType()
        trace.bullet = self
        trace.currentPosition = self.currentPosition.copy()
        trace.startPosition = self.currentPosition.copy()
        minTraceLength = self.velocity.copy()
        minTraceLength.setLength(0.01)
        trace.startPosition.sub(minTraceLength)

        return trace

    def makeExplosion(self):
        if self.explosionType is None:
            return None

        explosion = self.explosionType()
        explosion.position = self.currentPosition.copy()

        return explosion

    def getModelMatrix(self):
        return (
            TransformMatrix4Builder()
            .translate(self.currentPosition.x, self.currentPosition.y, self.currentPosition.z)
            .rotate(self.yawRadians, CommonConstants.zAxis)
            .rotate(self.pitchRadians, CommonConstants.xAxis)
            .rotate(self.rollRadians, CommonConstants.yAxis)
            .resultMatrix
        )
