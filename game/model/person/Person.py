from game.anx.CommonConstants import CommonConstants
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.level.Floor import Floor


class Person:

    def __init__(self):
        self.currentCenterPoint = Vector3()
        self.nextCenterPoint = self.currentCenterPoint.copy()
        self.collisionLevelSegments = set()
        self.currentFloor = Floor()
        self.health = CommonConstants.maxPersonHealth

    def addHealth(self, health):
        self.health = Math.min(self.health + health, CommonConstants.maxPersonHealth)
