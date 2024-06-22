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
        self.currentCenterPoint = Vector3(1.5, 1.5, 0)
        self.currentBorder = Box3d(PlayerMeasures.xyLength, PlayerMeasures.xyLength, PlayerMeasures.zLength)
        self.currentBorder.bottom.downLeft = Vector3(1, 1, 0)
        self.currentBorder.bottom.downRight = Vector3(2, 1, 0)
        self.currentBorder.bottom.upLeft = Vector3(1, 2, 0)
        self.currentBorder.bottom.upRight = Vector3(2, 2, 0)
        self.nextCenterPoint = self.currentCenterPoint.getCopy()
        self.nextBorder = self.currentBorder.getCopy()
        self.pitchRadians = 0
        self.yawRadians = 0
        self.lookDirection = Constants.yAxis
        self.frontNormal = Constants.yAxis
        self.rightNormal = Constants.xAxis
        self.hasMoved = False
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

    def commitNextPosition(self):
        self.currentCenterPoint = self.nextCenterPoint.getCopy()
        self.currentBorder = self.nextBorder.getCopy()
