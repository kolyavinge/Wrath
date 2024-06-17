from game.anx.Constants import Constants
from game.calc.Rect3d import Rect3d
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.level.LevelSegment import LevelSegment
from game.model.PlayerMeasures import PlayerMeasures
from game.model.VelocityFunc import VelocityFunc


class Person:

    maxPitchRadians = Math.piHalf - 0.1

    def __init__(self):
        self.currentCenterPoint = Vector3(1.5, 1.5, 0)
        self.currentBorder = Rect3d()
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
        self.floorIndex = 0
        self.levelSegments = [LevelSegment(0, 0, 0, 0)]

    def getVelocity(self):
        return self.velocityFunc.getValue(self.movingTime)

    def moveByVector(self, vector):
        self.nextCenterPoint.add(vector)
        self.nextBorder.moveByVector(vector)

    def moveCenterPointTo(self, x, y):
        self.nextCenterPoint.x = x
        self.nextCenterPoint.y = y
        self.nextBorder.bottom.downLeft = Vector3(x - PlayerMeasures.widthAndLengthHalf, y - PlayerMeasures.widthAndLengthHalf, 0)
        self.nextBorder.bottom.downRight = Vector3(x + PlayerMeasures.widthAndLengthHalf, y - PlayerMeasures.widthAndLengthHalf, 0)
        self.nextBorder.bottom.upLeft = Vector3(x - PlayerMeasures.widthAndLengthHalf, y + PlayerMeasures.widthAndLengthHalf, 0)
        self.nextBorder.bottom.upRight = Vector3(x + PlayerMeasures.widthAndLengthHalf, y + PlayerMeasures.widthAndLengthHalf, 0)

    def commitNextPosition(self):
        self.currentCenterPoint = self.nextCenterPoint.getCopy()
        self.currentBorder = self.nextBorder.getCopy()
