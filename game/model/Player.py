from game.anx.Constants import Constants
from game.calc.Box3d import Box3d
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.level.LevelSegment import LevelSegment
from game.model.PlayerMeasures import PlayerMeasures
from game.model.VelocityFunc import VelocityFunc


class Player:

    maxPitchRadians = Math.piHalf - 0.1

    def __init__(self):
        self.currentCenterPoint = Vector3()
        self.currentBorder = Box3d(PlayerMeasures.xyLength, PlayerMeasures.xyLength, PlayerMeasures.zLength)
        self.nextCenterPoint = self.currentCenterPoint.getCopy()
        self.nextBorder = self.currentBorder.getCopy()
        self.pitchRadians = 0
        self.yawRadians = 0
        self.lookDirection = Constants.yAxis
        self.frontNormal = Constants.yAxis
        self.rightNormal = Constants.xAxis
        self.hasMoved = False
        self.hasTurned = False
        self.movingTime = 1
        self.movingTimeDelta = 0.1
        self.velocityFunc = VelocityFunc()
        self.levelSegments = [LevelSegment()]

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
        self.currentCenterPoint = self.nextCenterPoint.getCopy()
        self.currentBorder = self.nextBorder.getCopy()
