from game.anx.CommonConstants import CommonConstants
from game.anx.PlayerConstants import PlayerConstants
from game.calc.Box3d import Box3d
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.VelocityFunc import VelocityFunc


class Player:

    maxPitchRadians = Math.piHalf - 0.1

    def __init__(self):
        self.currentCenterPoint = Vector3()
        self.currentBorder = Box3d(PlayerConstants.xyLength, PlayerConstants.xyLength, PlayerConstants.zLength)
        self.nextCenterPoint = self.currentCenterPoint.copy()
        self.nextBorder = self.currentBorder.copy()
        self.pitchRadians = 0
        self.yawRadians = 0
        self.lookDirection = CommonConstants.yAxis
        self.frontNormal = CommonConstants.yAxis
        self.rightNormal = CommonConstants.xAxis
        self.hasMoved = False
        self.hasTurned = False
        self.movingTime = 1
        self.movingTimeDelta = 0.1
        self.velocityFunc = VelocityFunc()
        self.collisionLevelSegments = set()
        self.visibilityLevelSegments = set()

    def getVelocity(self):
        return self.velocityFunc.getValue(self.movingTime)

    def moveNextPositionBy(self, vector):
        self.nextCenterPoint.add(vector)
        self.nextBorder.calculatePointsByCenter(self.nextCenterPoint)

    def moveNextPositionTo(self, vector):
        self.nextCenterPoint = vector
        self.nextBorder.calculatePointsByCenter(self.nextCenterPoint)

    def getZ(self):
        return self.nextCenterPoint.z

    def setZ(self, z):
        self.nextCenterPoint.z = z
        self.nextBorder.calculatePointsByCenter(self.nextCenterPoint)

    def commitNextPosition(self):
        self.currentCenterPoint = self.nextCenterPoint.copy()
        self.currentBorder = self.nextBorder.copy()
