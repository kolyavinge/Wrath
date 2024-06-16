from game.anx.Constants import Constants
from game.calc.Rect3d import Rect3d
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.level.LevelSegment import LevelSegment
from game.model.VelocityFunc import VelocityFunc


class Person:

    maxPitchRadians = Math.piHalf - 0.1

    def __init__(self):
        self.currentCenterPoint = Vector3(2, 2, 0)
        self.currentBorder = Rect3d()
        self.nextCenterPoint = Vector3(2, 2, 0)
        self.nextBorder = Rect3d()
        self.pitchRadians = 0
        self.yawRadians = 0
        self.lookDirection = Constants.yAxis
        self.frontNormal = Constants.yAxis
        self.rightNormal = Constants.xAxis
        self.hasMoved = False
        self.movingTime = 1
        self.movingTimeDelta = 0.1
        self.velocityFunc = VelocityFunc()
        self.floorIndex = 0
        self.levelSegment = LevelSegment(0, 0, 0, 0)

    def getVelocity(self):
        return self.velocityFunc.getValue(self.movingTime)

    def moveByVector(self, vector):
        self.nextCenterPoint.add(vector)
        self.nextBorder.moveByVector(vector)

    def commitNextPosition(self):
        self.currentCenterPoint = self.nextCenterPoint.getCopy()
        self.currentBorder = self.nextBorder.getCopy()
