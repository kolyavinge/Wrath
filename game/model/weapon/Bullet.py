from game.anx.CommonConstants import CommonConstants
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.calc.Vector3 import Vector3


class Bullet:

    def __init__(self):
        self.isVisible = False
        self.currentPosition = Vector3()
        self.nextPosition = Vector3()
        self.yawRadians = 0
        self.pitchRadians = 0
        self.velocity = Vector3()
        self.velocityValue = 0
        self.damage = 0
        self.totalDistance = 0
        self.currentLevelSegment = None
        self.nextLevelSegment = None
        self.currentVisibilityLevelSegment = None
        self.holeInfo = None

    def commitNextPosition(self):
        self.currentPosition = self.nextPosition.copy()

    def update(self):
        pass

    def getModelMatrix(self):
        return (
            TransformMatrix4Builder()
            .translate(self.currentPosition.x, self.currentPosition.y, self.currentPosition.z)
            .rotate(self.yawRadians, CommonConstants.zAxis)
            .rotate(self.pitchRadians, CommonConstants.xAxis)
            .resultMatrix
        )
