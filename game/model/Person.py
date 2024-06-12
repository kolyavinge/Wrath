from game.calc.Vector3 import Vector3
from game.model.VelocityFunc import VelocityFunc


class Person:

    def __init__(self):
        self.centerPoint = Vector3()
        self.lookDirection = Vector3(0, 1, 0)
        self.frontNormal = Vector3(0, 1, 0)
        self.rightNormal = Vector3(1, 0, 0)
        self.hasMoved = False
        self.movingTime = 0
        self.movingTimeDelta = 0.1
        self.velocityFunc = VelocityFunc()
        self.floorIndex = 0

    def getVelocity(self):
        return self.velocityFunc.getValue(self.movingTime)
