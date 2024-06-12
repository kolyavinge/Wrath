from game.lib.Math import Math
from game.calc.Vector3 import Vector3
from game.anx.Constants import Constants
from game.model.VelocityFunc import VelocityFunc


class Person:

    maxPitchRadians = Math.piHalf - 0.1

    def __init__(self):
        self.centerPoint = Vector3(2, 2, 0)
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

    def getVelocity(self):
        return self.velocityFunc.getValue(self.movingTime)
