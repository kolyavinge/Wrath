from game.anx.CommonConstants import CommonConstants
from game.anx.PersonConstants import PersonConstants
from game.calc.Box3d import Box3d
from game.calc.TransformMatrix4Builder import TransformMatrix4Builder
from game.calc.Vector3 import Vector3
from game.lib.Math import Math
from game.model.level.Floor import Floor
from game.model.level.LevelSegment import LevelSegment
from game.model.person.FallingFunc import FallingFunc
from game.model.person.PersonState import PersonState
from game.model.person.VelocityFunc import VelocityFunc


class Person:

    def __init__(self):
        self.state = PersonState.standing
        self.currentCenterPoint = Vector3()
        self.nextCenterPoint = self.currentCenterPoint.copy()
        self.collisionLevelSegments = set()
        self.visibilityLevelSegment = LevelSegment()
        self.currentBorder = Box3d(PersonConstants.xyLength, PersonConstants.xyLength, PersonConstants.zLength)
        self.nextBorder = self.currentBorder.copy()
        self.pitchRadians = 0
        self.yawRadians = 0
        self.lookDirection = CommonConstants.yAxis
        self.lookDirectionNormal = CommonConstants.zAxis
        self.frontNormal = CommonConstants.yAxis
        self.rightNormal = CommonConstants.xAxis
        self.hasMoved = False
        self.hasTurned = False
        self.forwardMovingTime = 0
        self.backwardMovingTime = 0
        self.leftStepMovingTime = 0
        self.rightStepMovingTime = 0
        self.movingTimeDelta = 0.1
        self.prevVelocityValue = 0
        self.velocityValue = 0
        self.velocityVector = Vector3()
        self.fallingTime = 0
        self.landingTime = 0
        self.velocityFunc = VelocityFunc()
        self.fallingFunc = FallingFunc()
        self.currentFloor = Floor()
        self.health = PersonConstants.maxPersonHealth

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

    def addHealth(self, health):
        if health < 0:
            raise Exception("health cannot be negative.")

        self.health = Math.min(self.health + health, PersonConstants.maxPersonHealth)

    def damage(self, value):
        if value < 0:
            raise Exception("value cannot be negative.")

        self.health = Math.max(self.health - value, 0)

    def getModelMatrix(self):
        return (
            TransformMatrix4Builder()
            .translate(self.currentCenterPoint.x, self.currentCenterPoint.y, self.currentCenterPoint.z)
            .rotate(self.yawRadians, CommonConstants.zAxis)
            .resultMatrix
        )
